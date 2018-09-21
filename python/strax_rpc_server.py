"""The Python implementation of the gRPC strax server."""

from concurrent import futures
import numpy as np
import pandas as pd
import strax
import time
import fnmatch
import grpc
import strax_rpc_pb2, strax_rpc_pb2_grpc

import config

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

dcolumns = {
  "int16": strax_rpc_pb2.Int32Column,
  "int32": strax_rpc_pb2.Int32Column,
  "int64": strax_rpc_pb2.Int64Column,
  "float32":strax_rpc_pb2.Float32Column,
  "float64":strax_rpc_pb2.Float64Column,
  "object": strax_rpc_pb2.StringColumn,
  "string": strax_rpc_pb2.StringColumn,
  "bool": strax_rpc_pb2.BoolColumn,
}

def fake_df(ncol=10,nrow=100):
    data = {}
    for c in range(ncol):
        data['col_{}'.format(c)] = np.random.random(nrow)
    return pd.DataFrame(data)

def df_to_columns(df):
    cols = []
    for name in df.columns:
        dtype = str(df[name].dtype)
        info = strax_rpc_pb2.ColumnInfo(
                  name=name,
                  dtype=dtype,
            )
        if dtype == "object":
            values = df[name].astype('str').values
        else:
            values = df[name].values

        data =  dcolumns[dtype](
            index=df[name].index,
            values=values,
            )
        cols.append(strax_rpc_pb2.DataColumn(**{'info': info, dtype:data}))
    return cols

def search_field(ctx, pattern, max_matches):
    """
    Temporary fix
    """
    match_list = []
    cache = dict()
    for d in ctx._plugin_class_registry:
        if d not in cache:
            cache.update(ctx._get_plugins((d,), run_id='0'))
        p = cache[d]

        for field_name in p.dtype.names:
            if fnmatch.fnmatch(field_name, pattern):
                if max_matches and len(match_list)>=max_matches:
                    return match_list
                match_list.append((field_name, d, p.__class__.__name__))
    return match_list

class StraxRPCServicer(strax_rpc_pb2_grpc.StraxRPCServicer):

    def __init__(self):
        print('Servicer started.')
        self.ctx = strax.Context(
            storage=[strax.ZipDirectory(config.ZIPDIR),
                     strax.DataDirectory(config.DATADIR)],
            register_all=strax.xenon.plugins)


    def SearchField(self, request, context):
        """
            TODO: Adapt search_field to accept flag for api usage of strax
            then change this method to:
                        match_list = self.ctx.search_field(pattern)
        """

        pattern = request.pattern
        max_matches = request.max_matches
        match_list = search_field(self.ctx, pattern, max_matches)
        for column, dataname, plugin in match_list:
            yield strax_rpc_pb2.ColumnInfo(
                  name=column,
                  data_name=dataname,
                  plugin=plugin,
                 )


    def DataInfo(self, request, context):
      """

      """
      dataname = request.name
      df = self.ctx.data_info(dataname)
      for col in df_to_columns(df):
          yield col

    def GetDF(self, request, context):
        plugin_name = request.name
        run_id = request.run_id
        try:
            df = self.ctx.get_df(run_id, plugin_name) #
        except:
            df = fake_df() #
        for col in df_to_columns(df):
            yield col

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    strax_rpc_pb2_grpc.add_StraxRPCServicer_to_server(
        StraxRPCServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
