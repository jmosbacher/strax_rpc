from __future__ import print_function
import grpc
from . import straxrpc_pb2
from . import straxrpc_pb2_grpc
import pandas as pd
import numpy as np
from collections import defaultdict


class StraxClientBase:

    def __init__(self, addr="localhost:50051"):
        self.addr = addr

    def stream_to_rows(self, stream):
        # FIXME: add index verification for each row
        row = {}
        dtypes = []
        for r in stream:
            if r.column not in row:
                name = r.WhichOneof("value")
                row[r.column] = [getattr(r, name)]
                dtypes.append(r.dtype)
            else:
                yield row, dtypes
                row = {}
                dtypes = []
        yield row, dtypes            

    def build_result(self, table, dtypes=None, return_type="df"):
        if return_type=="df":
            result = pd.DataFrame(table)
        elif return_type=="array":
            if dtypes is None:
                fmts = [None]*len(table.keys())
            else:
                fmts = dtypes
            result = np.fromiter(zip(*[c for c in table.values()]), dtype={"names": list(table.keys()), "formats":fmts})
        return result

    def stream_to_table(self, stream, return_type="df"):
        # FIXME: check dtypes 
        data = defaultdict(list)
        for row, dtypes in self.stream_to_rows(stream):
            for k, v in row.items():
                data[k].extend(v)
        return self.build_result(data, dtypes,return_type)    
            

    def search_field(self, pattern):
         with grpc.insecure_channel(self.addr) as channel:
            stub = straxrpc_pb2_grpc.StraxRPCStub(channel)
            sp = straxrpc_pb2.SearchPattern(pattern=pattern)
            rs = stub.SearchField(sp)
            results = [f"{r.name} is part of {r.data_name} (provided by {r.plugin})" for r in rs]
            # print(results)
            return results

    def data_info_stream(self, dataname, channel):
        stub = straxrpc_pb2_grpc.StraxRPCStub(channel)
        ti = straxrpc_pb2.TableInfo(name=dataname)
        return stub.DataInfo(ti)
        

    def get_df_stream(self, run_id, dframe, channel):
        
        stub = straxrpc_pb2_grpc.StraxRPCStub(channel)
        ti = straxrpc_pb2.TableInfo(name=dframe, run_id=run_id)
        return stub.GetDataframe(ti)

    

    def get_array_stream(self, run_id, dframe, channel):

        stub = straxrpc_pb2_grpc.StraxRPCStub(channel)
        ti = straxrpc_pb2.TableInfo(name=dframe, run_id=run_id)
        # f = straxrpc_pb2.ColumnInfo(name='random')
        return stub.GetArray(ti)

    def show_config_stream(self, name, channel):
        stub = straxrpc_pb2_grpc.StraxRPCStub(channel)
        ti = straxrpc_pb2.TableInfo(name=name)
        return stub.ShowConfig(ti)

    def search_dataframe_names(self, pattern):
        with grpc.insecure_channel(self.addr) as channel:
            stub = straxrpc_pb2_grpc.StraxRPCStub(channel)
            sp = straxrpc_pb2.SearchPattern(pattern=pattern,)
            rs = stub.SearchDataframeNames(sp)
            names = [x.name for x in rs]
            # print(names)
            return names


            # data = {}
            # for col in stub.ShowConfig(ti):
            #     vs = getattr(col, col.info.dtype).values
            #     data[col.info.name] = pd.Series(index=col.index, data=vs)
            # df = pd.DataFrame(data)
            # return df

class StraxClient(StraxClientBase):

    def data_info(self, dataname):
        with grpc.insecure_channel(self.addr) as channel:
            stream = self.data_info_stream(dataname, channel)
            self.stream_to_table(stream)

    def get_df(self, run_id, dframe):
        with grpc.insecure_channel(self.addr) as channel:
            stream = self.get_array_stream(run_id, dframe, channel)
            return self.stream_to_table(stream)

    def get_array(self, run_id, dframe):
        with grpc.insecure_channel(self.addr) as channel:
            stream = self.get_array_stream( run_id, dframe, channel)
            return self.stream_to_table(stream, return_type="array")

    def show_config(self, name):
        with grpc.insecure_channel(self.addr) as channel:
            stream = self.show_config_stream(name, channel)
            return self.stream_to_table(stream)

class StraxStreamClient(StraxClientBase):

    def data_info(self, dataname):
        channel = grpc.insecure_channel(self.addr)
        stream = self.data_info_stream(dataname, channel)
        for row, fmts in self.stream_to_rows(stream):
            df = self.build_result(row, fmts)
            yield df
        channel.close()

    def get_df(self, run_id, dframe):
        with grpc.insecure_channel(self.addr) as channel:
            stream = self.get_array_stream(run_id, dframe, channel)
            for row, fmts in self.stream_to_rows(stream):
                yield self.build_result(row, fmts)
       
    def get_array(self, run_id, dframe):
        with grpc.insecure_channel(self.addr) as channel:
            stream = self.get_array_stream( run_id, dframe, channel)
            for row, fmts in self.stream_to_rows(stream):
                yield self.build_result(row, fmts, return_type="array")

    def show_config(self, name):
        with grpc.insecure_channel(self.addr) as channel:
            stream = self.show_config_stream(name, channel)
            for row, fmts in self.stream_to_rows(stream):

                yield self.build_result(row, fmts)

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
