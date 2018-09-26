from __future__ import print_function
import grpc
from . import straxrpc_pb2
from . import straxrpc_pb2_grpc
import pandas as pd
import numpy as np


class StraxClient:
    def __init__(self, addr="localhost", port=50051):
        self.addr = addr
        self.port = port

    def search_field(self, pattern, max_matches=10):
         with grpc.insecure_channel('{}:{}'.format(self.addr,self.port)) as channel:
            stub = straxrpc_pb2_grpc.StraxRPCStub(channel)
            sp = straxrpc_pb2.SearchPattern(
                pattern=pattern,
                max_matches=max_matches,
            )
            rs = stub.SearchField(sp)
            results = [f"{r.name} is part of {r.data_name} (provided by {r.plugin})" for r in rs]
            # print(results)
            return results

    def data_info(self,dataname):
        with grpc.insecure_channel('{}:{}'.format(self.addr,self.port)) as channel:
            stub = straxrpc_pb2_grpc.StraxRPCStub(channel)
            pi = straxrpc_pb2.PluginInfo(name=dataname)
        
            data = {}
            for col in stub.DataInfo(pi):
                vs = getattr(col, col.info.dtype).values
                data[col.info.name] = pd.Series(index=col.index, data=vs)
            df = pd.DataFrame(data)
            return df

    def get_df(self, run_id, dframe):
        with grpc.insecure_channel('{}:{}'.format(self.addr,self.port)) as channel:
            stub = straxrpc_pb2_grpc.StraxRPCStub(channel)
            ti = straxrpc_pb2.TableInfo(name=dframe, run_id=run_id)
            data = {}
            for col in stub.GetDataframe(ti):
                vs = getattr(col, col.info.dtype).values
                data[col.info.name] = pd.Series(index=col.index, data=vs)
            df = pd.DataFrame(data)
            return df

    def get_array(self, run_id, dframe):
        with grpc.insecure_channel('{}:{}'.format(self.addr,self.port)) as channel:
            stub = straxrpc_pb2_grpc.StraxRPCStub(channel)
            ti = straxrpc_pb2.TableInfo(name=dframe, run_id=run_id)
            # f = straxrpc_pb2.ColumnInfo(name='random')
            data = []
            names = []
            formats = []

            for col in stub.GetArray(ti):
                vs = getattr(col, col.info.dtype).values
                data.append(vs)
                names.append(col.info.name)
                formats.append(col.info.dtype)
            
            dtype = dict(names = names, formats=formats)
            arr = np.fromiter(zip(*data), dtype=dtype)
            return arr

    def search_dataframe_names(self, pattern, max_matches=10):
        with grpc.insecure_channel('{}:{}'.format(self.addr,self.port)) as channel:
            stub = straxrpc_pb2_grpc.StraxRPCStub(channel)
            sp = straxrpc_pb2.SearchPattern(
                pattern=pattern,
                max_matches=max_matches,
            )
            rs = stub.SearchDataframeNames(sp)
            names = [x.name for x in rs]
            print(names)
            return names

def run():
    client = StraxClient()
    print("---------------------- Search for s1* ----------------------")
    res = client.search_field( "s1*")
    print("\n".join(res))
    print("\n-------------- Data Info for event_basics --------------\n")
    df = client.data_info( 'event_basics')
    print(df)
    print("\n--------- Get event_basics df for 180423_1021 ---------\n")
    df = client.get_df( '180423_1021', 'event_basics')
    print(df)
    print("\n--------- Get event_basics array for 180423_1021 ---------\n")
    arr = client.get_array( '180423_1021', 'event_basics')
    print(arr.dtype.names)
    print(arr)

if __name__ == '__main__':
    run()
