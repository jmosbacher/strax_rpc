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

_ONE_DAY_IN_SECONDS = 60 * 60 * 24



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

def table_to_values(table):
    if isinstance(table, dict):
        keys = list(table.keys())
        dtype_names = [str(type(table[k][0]) for k in keys)]
    elif isinstance(table, np.ndarray):
        keys = list(table.dtype.names)
        dtype_names = [str(table.dtype[i]) for i, _ in enumerate(table.dtype.names)]
    elif isinstance(table, pd.DataFrame):
        keys = list(table.columns)
        dtype_names = [str(table[k].dtype) for k in keys]
    else:
        return None
    testers = []
    for name in dtype_names:
        for tester in type_testers:
            if tester.test(name):
                testers.append(tester)
                break 
    for i, vals in enumerate(zip(*[table[k] for k in keys])):
        for k, v, t in zip(keys, vals, testers):
            kwargs = {
                "index": i,
                "column": k,
                "dtype": t.name,
                t.name: t.cast(v),
            }
            yield straxrpc_pb2.TableValue(**kwargs)


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
      dataname = request.name
      df = self.ctx.data_info(dataname)
      for val in table_to_values(df):
          yield val

    def GetDataframe(self, request, context):
        plugin_name = request.name
        run_id = request.run_id
        try:
            df = self.ctx.get_df(run_id, plugin_name) #
        except:
            columns = self.ctx.data_info(plugin_name)["Field name"].values
            df = empty_df(columns) #
        for v in table_to_values(df):
            yield v

    def GetArray(self, request, context):
        plugin_name = request.name
        run_id = request.run_id
        try:
            arr = self.ctx.get_array(run_id, plugin_name) #
        except:
            columns = self.ctx.data_info(plugin_name)["Field name"].values
            df = empty_df(columns) #
        for v in table_to_values(arr):
            yield v

    def SearchDataframeNames(self, request, context):
        pattern = request.pattern
        for d in self.ctx._plugin_class_registry:
            if fnmatch.fnmatch(d, pattern):
                yield straxrpc_pb2.PluginInfo(name=d,)

    def ShowConfig(self, request, context):
        name = request.name
        df = self.ctx.show_config(name)
        for v in table_to_values(df):
            yield v

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

