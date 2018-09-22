from __future__ import print_function
import grpc
import strax_rpc_pb2, strax_rpc_pb2_grpc
import pandas as pd

def search_field(stub, pattern, max_matches=10):
    sp = strax_rpc_pb2.SearchPattern(
        pattern=pattern,
        max_matches=max_matches,
    )
    rs = stub.SearchField(sp)
    for r in rs:
        print(f"{r.name} is part of {r.data_name} (provided by {r.plugin})")

def data_info(stub, dataname):
    pi = strax_rpc_pb2.PluginInfo(name=dataname)
    # rs = stub.DataInfo(pi)
    data = {}
    for col in stub.DataInfo(pi):
        d = getattr(col, col.info.dtype)
        data[col.info.name] = pd.Series(index=d.index, data=d.values)
    df = pd.DataFrame(data)

    # t = PrettyTable()
    # t.field_names = ['index','Data name', 'Field name', 'Comment']
    # for i,r in enumerate(rs):
    #     t.add_row([i, r.name, r.dtype, r.comment ])
    print(df)

def get_df(stub,run_id,dframe):
    ti = strax_rpc_pb2.TableInfo(name=dframe, run_id=run_id)
    # f = strax_rpc_pb2.ColumnInfo(name='random')
    data = {}
    for col in stub.GetDF(ti):
        d = getattr(col, col.info.dtype)
        data[col.info.name] = pd.Series(index=d.index, data=d.values)
        # print(col.info.name, ' ', col.info.dtype)
        # for i,v in zip(r.index, r.value):
        #     print(f'{i} : {v}')
    df = pd.DataFrame(data)
    print(df)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = strax_rpc_pb2_grpc.StraxRPCStub(channel)
        print("---------------------- Search for s1* ----------------------")
        search_field(stub, "s1*")
        print("\n-------------- Data Info for event_basics --------------\n")
        data_info(stub, 'event_basics')
        print("\n----------- Get event_basics for 180423_1021 -----------\n")
        get_df(stub, '180423_1021', 'event_basics')


if __name__ == '__main__':
    run()
