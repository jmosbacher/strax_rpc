"""The Python implementation of the gRPC strax server."""

from concurrent import futures
import numpy as np
import pandas as pd
import time
import fnmatch
import grpc
from . import straxrpc_pb2
from . import straxrpc_pb2_grpc
from .data_types import type_testers
import pickle
from serializers import serializers

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
MAXBYTES = 10**5




def fake_df(ncol=10,nrow=10):
    data = {}
    for c in range(ncol):
        data['col_{}'.format(c)] = np.random.random(nrow)
    return pd.DataFrame(data)

def empty_df(columns):
    data = {col:[] for col in columns}
    return pd.DataFrame(data)

def fake_arr(ncol=10,nrow=10):
    a = np.random.random((nrow,ncol))
    a.dtype=np.dtype([(('random column number {}'.format(c),'col_{}'.format(c)),np.float64) for c in range(ncol)])
    return a

def empty_arr(names, dtypes):
    arr = np.fromiter(zip(*[[]*len(names)]), dtype={"names":names, "formats": dtypes})
    return arr


def search_field(ctx, pattern):
    """
    Temporary fix, need to add pull request to have a flag to change this methods
    behavior so it returns a machine readable structure instead of printing to stdout.
    """
    match_list = []
    cache = dict()
    for d in ctx._plugin_class_registry:
        if d not in cache:
            cache.update(ctx._get_plugins((d,), run_id='0'))
        p = cache[d]

        for field_name in p.dtype.names:
            if fnmatch.fnmatch(field_name, pattern):
                match_list.append((field_name, d, p.__class__.__name__))
    return match_list

class StraxRPCServicer(straxrpc_pb2_grpc.StraxRPCServicer):

    def __init__(self, strax_context):
        print('Servicer started.')
        self.ctx = strax_context
        
    def array_to_chunks(self, arr, serializer="pickle"):
        nmsgs = max(arr.nbytes//MAXBYTES,1)
        parts = np.array_split(arr, nmsgs)
        for part in parts:
            msg = serializers[serializer].array_to_bytes(part)
            # msg = pickle.dumps(part)
            yield straxrpc_pb2.ArrayChunk(data=msg, nrows=part.size, serializer=serializer, compression='none')

    def SearchField(self, request, context):
        """
            TODO: Adapt search_field to accept flag for api usage of strax
            then change this method to:
                        match_list = self.ctx.search_field(pattern)
        """

        pattern = request.pattern
   
        match_list = search_field(self.ctx, pattern)
        for column, dataname, plugin in match_list:
            yield straxrpc_pb2.ColumnInfo(
                  name=column,
                  data_name=dataname,
                  plugin=plugin,
                 )


    def DataInfo(self, request, context):
      """

      """
      name = request.names[0]
      df = self.ctx.data_info(name)
      serializer = request.serializer
      if not serializer:
        serializer = "pickle"
      msg = serializers[serializer].df_to_bytes(df.astype("str"))
      return straxrpc_pb2.Dataframe(data=msg, serializer="serializer", nrows=len(df.index))

    def GetArray(self, request, context):
        plugin_names = [name for name in request.names]
        run_id = request.run_id
        serializer = request.serializer
        if not serializer:
            serializer = "pickle"
        try:
            for arr in self.ctx.get_iter(run_id, plugin_names):
                for r in self.array_to_chunks(arr, serializer=serializer):
                    yield r
        except:
            info = pd.concat([self.ctx.data_info(plugin_name) for plugin_name in plugin_names])
            columns = list(info["Field name"])
            dtypes = list(info["Data type"])
            arr = empty_arr(columns, dtypes)
            for r in self.array_to_chunks(arr, serializer=serializer):
                    yield r
        
    def SearchDataframeNames(self, request, context):
        pattern = request.pattern
        for d in self.ctx._plugin_class_registry:
            if fnmatch.fnmatch(d, pattern):
                yield straxrpc_pb2.PluginInfo(name=d,)

    def ShowConfig(self, request, context):
        name = request.names[0]
        serializer = request.serializer
        if not serializer:
            serializer = "pickle"
        df = self.ctx.show_config(name)
        msg = serializers[serializer].df_to_bytes(df)
        # msg = pickle.dumps(df)
        return straxrpc_pb2.Dataframe(data=msg, serializer=serializer, nrows=len(df.index))

class StraxServer:
    def __init__(self, addr="localhost:50051", strax_context=None):
        self.addr = addr

    def serve(self, strax_context):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        straxrpc_pb2_grpc.add_StraxRPCServicer_to_server(
            StraxRPCServicer(strax_context), server)
        server.add_insecure_port(self.addr)
        server.start()
        try:
            while True:
                time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
            server.stop(0)

