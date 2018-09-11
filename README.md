# StraxRPC
A proof-of-concept RPC server and client pair for the strax framework.
Based on the gRPC framework and currently server and clients only implemented in python.

## Getting started
To run the server:
- pip install:
   - strax
   - grpcio
- Change the location of the sample files in config.py
- run "python strax_rpc_server.py"

To run the client:
- pip install grpcio
- run "python strax_rpc_client.py" or import the file and use the sample functions directly.
