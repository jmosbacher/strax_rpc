"""The Python implementation of the gRPC route guide server."""

from concurrent import futures
import numpy as np
import pandas as pd
import strax
import time
import math
import fnmatch
import grpc

import strax_rpc_pb2
import strax_rpc_pb2_grpc
import config

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

ctx = strax.Context(
    storage=[strax.ZipDirectory(config.ZIPDIR),
             strax.DataDirectory(config.DATADIR)],
    register_all=strax.xenon.plugins)

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
        self.ctx = ctx

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
            yield strax_rpc_pb2.Match(
                  column=column,
                  dataname=dataname,
                  plugin=plugin,
                 )


    def DataInfo(self, request, context):
      """

      """
      dataname = request.name
      df = self.ctx.data_info(dataname)
      for idx,row in df.iterrows():
          yield strax_rpc_pb2.Field(
                index=idx,
                name=row['Field name'],
                dtype=str(row['Data type']),
                comment=row['Comment'],
               )
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
