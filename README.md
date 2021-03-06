# StraxRPC
A proof-of-concept RPC server and client pair for the strax framework.
Based on the gRPC framework and currently server and clients only implemented in python.

## Getting started
To run the server:
- pip install:
   - strax
   - grpcio
   - straxrpc

- Run a Python script with the following code:
``` python
    
    from straxrpc import StraxServer
    import strax
    server = StraxServer()
    ctx = strax.Context(
            storage=[strax.ZipDirectory('./processed'),
                     strax.DataDirectory('./custom_data')],
            register_all=strax.xenon.plugins)
    server.serve(ctx)

```

To run the client:
- pip install grpcio
- run "python strax_rpc_client.py" or import the file and use the sample functions directly.
- The node client can be created dynamically by grpc from the proto file. An example can be found in node/strax_rpc_client.js 
