from grpc_tools import protoc

protoc.main((
    '',
    '-I../protos/',
    '--python_out=./straxrpc/',
    '--grpc_python_out=./straxrpc/',
    '../protos/straxrpc/straxrpc.proto',
))
