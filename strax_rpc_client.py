
from __future__ import print_function

import random

import grpc

import strax_rpc_pb2
import strax_rpc_pb2_grpc

from prettytable import PrettyTable

def search_field(stub, pattern, max_matches=10):
    sp = strax_rpc_pb2.SearchPattern(
        pattern=pattern,
        max_matches=max_matches,
    )
    rs = stub.SearchField(sp)
    for r in rs:
        print(f"{r.column} is part of {r.dataname} (provided by {r.plugin})")

def data_info(stub, dataname):
    dn = strax_rpc_pb2.DataName(name=dataname)
    rs = stub.DataInfo(dn)
    t = PrettyTable()
    t.field_names = ['index','Data name', 'Field name', 'Comment']
    for r in rs:
        t.add_row([r.index, r.name, r.dtype, r.comment ])
    print(t)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = strax_rpc_pb2_grpc.StraxRPCStub(channel)
        print("-------------------- Search for s1* --------------------")
        search_field(stub, "s1*")
        print("\n-------------- Data Info for event_basics --------------\n")
        data_info(stub, 'event_basics')



if __name__ == '__main__':
    run()
