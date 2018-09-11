# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import strax_rpc_pb2 as strax__rpc__pb2


class StraxRPCStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SearchField = channel.unary_stream(
        '/straxrpc.StraxRPC/SearchField',
        request_serializer=strax__rpc__pb2.SearchPattern.SerializeToString,
        response_deserializer=strax__rpc__pb2.ColumnInfo.FromString,
        )
    self.DataInfo = channel.unary_stream(
        '/straxrpc.StraxRPC/DataInfo',
        request_serializer=strax__rpc__pb2.PluginInfo.SerializeToString,
        response_deserializer=strax__rpc__pb2.DataColumn.FromString,
        )
    self.GetDF = channel.unary_stream(
        '/straxrpc.StraxRPC/GetDF',
        request_serializer=strax__rpc__pb2.TableInfo.SerializeToString,
        response_deserializer=strax__rpc__pb2.DataColumn.FromString,
        )


class StraxRPCServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SearchField(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DataInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetDF(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StraxRPCServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SearchField': grpc.unary_stream_rpc_method_handler(
          servicer.SearchField,
          request_deserializer=strax__rpc__pb2.SearchPattern.FromString,
          response_serializer=strax__rpc__pb2.ColumnInfo.SerializeToString,
      ),
      'DataInfo': grpc.unary_stream_rpc_method_handler(
          servicer.DataInfo,
          request_deserializer=strax__rpc__pb2.PluginInfo.FromString,
          response_serializer=strax__rpc__pb2.DataColumn.SerializeToString,
      ),
      'GetDF': grpc.unary_stream_rpc_method_handler(
          servicer.GetDF,
          request_deserializer=strax__rpc__pb2.TableInfo.FromString,
          response_serializer=strax__rpc__pb2.DataColumn.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'straxrpc.StraxRPC', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
