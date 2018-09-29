# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from straxrpc import straxrpc_pb2 as straxrpc_dot_straxrpc__pb2


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
        request_serializer=straxrpc_dot_straxrpc__pb2.SearchPattern.SerializeToString,
        response_deserializer=straxrpc_dot_straxrpc__pb2.ColumnInfo.FromString,
        )
    self.SearchDataframeNames = channel.unary_stream(
        '/straxrpc.StraxRPC/SearchDataframeNames',
        request_serializer=straxrpc_dot_straxrpc__pb2.SearchPattern.SerializeToString,
        response_deserializer=straxrpc_dot_straxrpc__pb2.PluginInfo.FromString,
        )
    self.DataInfo = channel.unary_stream(
        '/straxrpc.StraxRPC/DataInfo',
        request_serializer=straxrpc_dot_straxrpc__pb2.TableInfo.SerializeToString,
        response_deserializer=straxrpc_dot_straxrpc__pb2.DataColumn.FromString,
        )
    self.GetDataframe = channel.unary_stream(
        '/straxrpc.StraxRPC/GetDataframe',
        request_serializer=straxrpc_dot_straxrpc__pb2.TableInfo.SerializeToString,
        response_deserializer=straxrpc_dot_straxrpc__pb2.DataColumn.FromString,
        )
    self.GetArray = channel.unary_stream(
        '/straxrpc.StraxRPC/GetArray',
        request_serializer=straxrpc_dot_straxrpc__pb2.TableInfo.SerializeToString,
        response_deserializer=straxrpc_dot_straxrpc__pb2.DataColumn.FromString,
        )
    self.ShowConfig = channel.unary_stream(
        '/straxrpc.StraxRPC/ShowConfig',
        request_serializer=straxrpc_dot_straxrpc__pb2.TableInfo.SerializeToString,
        response_deserializer=straxrpc_dot_straxrpc__pb2.DataColumn.FromString,
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

  def SearchDataframeNames(self, request, context):
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

  def GetDataframe(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetArray(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ShowConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StraxRPCServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SearchField': grpc.unary_stream_rpc_method_handler(
          servicer.SearchField,
          request_deserializer=straxrpc_dot_straxrpc__pb2.SearchPattern.FromString,
          response_serializer=straxrpc_dot_straxrpc__pb2.ColumnInfo.SerializeToString,
      ),
      'SearchDataframeNames': grpc.unary_stream_rpc_method_handler(
          servicer.SearchDataframeNames,
          request_deserializer=straxrpc_dot_straxrpc__pb2.SearchPattern.FromString,
          response_serializer=straxrpc_dot_straxrpc__pb2.PluginInfo.SerializeToString,
      ),
      'DataInfo': grpc.unary_stream_rpc_method_handler(
          servicer.DataInfo,
          request_deserializer=straxrpc_dot_straxrpc__pb2.TableInfo.FromString,
          response_serializer=straxrpc_dot_straxrpc__pb2.DataColumn.SerializeToString,
      ),
      'GetDataframe': grpc.unary_stream_rpc_method_handler(
          servicer.GetDataframe,
          request_deserializer=straxrpc_dot_straxrpc__pb2.TableInfo.FromString,
          response_serializer=straxrpc_dot_straxrpc__pb2.DataColumn.SerializeToString,
      ),
      'GetArray': grpc.unary_stream_rpc_method_handler(
          servicer.GetArray,
          request_deserializer=straxrpc_dot_straxrpc__pb2.TableInfo.FromString,
          response_serializer=straxrpc_dot_straxrpc__pb2.DataColumn.SerializeToString,
      ),
      'ShowConfig': grpc.unary_stream_rpc_method_handler(
          servicer.ShowConfig,
          request_deserializer=straxrpc_dot_straxrpc__pb2.TableInfo.FromString,
          response_serializer=straxrpc_dot_straxrpc__pb2.DataColumn.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'straxrpc.StraxRPC', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
