// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var strax_rpc_pb = require('./strax_rpc_pb.js');

function serialize_straxrpc_ColumnInfo(arg) {
  if (!(arg instanceof strax_rpc_pb.ColumnInfo)) {
    throw new Error('Expected argument of type straxrpc.ColumnInfo');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_straxrpc_ColumnInfo(buffer_arg) {
  return strax_rpc_pb.ColumnInfo.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_straxrpc_DataColumn(arg) {
  if (!(arg instanceof strax_rpc_pb.DataColumn)) {
    throw new Error('Expected argument of type straxrpc.DataColumn');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_straxrpc_DataColumn(buffer_arg) {
  return strax_rpc_pb.DataColumn.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_straxrpc_PluginInfo(arg) {
  if (!(arg instanceof strax_rpc_pb.PluginInfo)) {
    throw new Error('Expected argument of type straxrpc.PluginInfo');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_straxrpc_PluginInfo(buffer_arg) {
  return strax_rpc_pb.PluginInfo.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_straxrpc_SearchPattern(arg) {
  if (!(arg instanceof strax_rpc_pb.SearchPattern)) {
    throw new Error('Expected argument of type straxrpc.SearchPattern');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_straxrpc_SearchPattern(buffer_arg) {
  return strax_rpc_pb.SearchPattern.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_straxrpc_TableInfo(arg) {
  if (!(arg instanceof strax_rpc_pb.TableInfo)) {
    throw new Error('Expected argument of type straxrpc.TableInfo');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_straxrpc_TableInfo(buffer_arg) {
  return strax_rpc_pb.TableInfo.deserializeBinary(new Uint8Array(buffer_arg));
}


var StraxRPCService = exports.StraxRPCService = {
  searchField: {
    path: '/straxrpc.StraxRPC/SearchField',
    requestStream: false,
    responseStream: true,
    requestType: strax_rpc_pb.SearchPattern,
    responseType: strax_rpc_pb.ColumnInfo,
    requestSerialize: serialize_straxrpc_SearchPattern,
    requestDeserialize: deserialize_straxrpc_SearchPattern,
    responseSerialize: serialize_straxrpc_ColumnInfo,
    responseDeserialize: deserialize_straxrpc_ColumnInfo,
  },
  dataInfo: {
    path: '/straxrpc.StraxRPC/DataInfo',
    requestStream: false,
    responseStream: true,
    requestType: strax_rpc_pb.PluginInfo,
    responseType: strax_rpc_pb.DataColumn,
    requestSerialize: serialize_straxrpc_PluginInfo,
    requestDeserialize: deserialize_straxrpc_PluginInfo,
    responseSerialize: serialize_straxrpc_DataColumn,
    responseDeserialize: deserialize_straxrpc_DataColumn,
  },
  getDF: {
    path: '/straxrpc.StraxRPC/GetDF',
    requestStream: false,
    responseStream: true,
    requestType: strax_rpc_pb.TableInfo,
    responseType: strax_rpc_pb.DataColumn,
    requestSerialize: serialize_straxrpc_TableInfo,
    requestDeserialize: deserialize_straxrpc_TableInfo,
    responseSerialize: serialize_straxrpc_DataColumn,
    responseDeserialize: deserialize_straxrpc_DataColumn,
  },
};

exports.StraxRPCClient = grpc.makeGenericClientConstructor(StraxRPCService);
