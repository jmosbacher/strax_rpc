# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: strax_rpc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='strax_rpc.proto',
  package='straxrpc',
  syntax='proto3',
  serialized_pb=_b('\n\x0fstrax_rpc.proto\x12\x08straxrpc\"5\n\rSearchPattern\x12\x0f\n\x07pattern\x18\x01 \x01(\t\x12\x13\n\x0bmax_matches\x18\x02 \x01(\r\")\n\tTableInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06run_id\x18\x02 \x01(\t\"U\n\nPluginInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nclass_name\x18\x02 \x01(\t\x12%\n\x07\x63olumns\x18\x03 \x03(\x0b\x32\x14.straxrpc.ColumnInfo\"]\n\nColumnInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tdata_name\x18\x02 \x01(\t\x12\x0e\n\x06plugin\x18\x03 \x01(\t\x12\x0f\n\x07\x63omment\x18\x04 \x01(\t\x12\r\n\x05\x64type\x18\x05 \x01(\t\"\x1c\n\nInt32Array\x12\x0e\n\x06values\x18\x01 \x03(\x05\"\x1c\n\nInt64Array\x12\x0e\n\x06values\x18\x01 \x03(\x03\"7\n\x0fInt32ArrayArray\x12$\n\x06values\x18\x01 \x03(\x0b\x32\x14.straxrpc.Int32Array\"7\n\x0fInt64ArrayArray\x12$\n\x06values\x18\x01 \x03(\x0b\x32\x14.straxrpc.Int64Array\"\x1b\n\tBoolArray\x12\x0e\n\x06values\x18\x01 \x03(\x08\"\x1e\n\x0c\x46loat32Array\x12\x0e\n\x06values\x18\x01 \x03(\x02\"\x1e\n\x0c\x46loat64Array\x12\x0e\n\x06values\x18\x01 \x03(\x01\";\n\x11\x46loat32ArrayArray\x12&\n\x06values\x18\x01 \x03(\x0b\x32\x16.straxrpc.Float32Array\";\n\x11\x46loat64ArrayArray\x12&\n\x06values\x18\x01 \x03(\x0b\x32\x16.straxrpc.Float64Array\"\x1d\n\x0bStringArray\x12\x0e\n\x06values\x18\x01 \x03(\t\"\xae\x04\n\nDataColumn\x12\"\n\x04info\x18\x63 \x01(\x0b\x32\x14.straxrpc.ColumnInfo\x12\r\n\x05index\x18\x01 \x03(\r\x12%\n\x05int32\x18\x02 \x01(\x0b\x32\x14.straxrpc.Int32ArrayH\x00\x12%\n\x05int64\x18\x03 \x01(\x0b\x32\x14.straxrpc.Int64ArrayH\x00\x12)\n\x07\x66loat32\x18\x04 \x01(\x0b\x32\x16.straxrpc.Float32ArrayH\x00\x12)\n\x07\x66loat64\x18\x05 \x01(\x0b\x32\x16.straxrpc.Float64ArrayH\x00\x12\'\n\x06string\x18\x06 \x01(\x0b\x32\x15.straxrpc.StringArrayH\x00\x12#\n\x04\x62ool\x18\x07 \x01(\x0b\x32\x13.straxrpc.BoolArrayH\x00\x12\'\n\x06object\x18\x08 \x01(\x0b\x32\x15.straxrpc.StringArrayH\x00\x12\x33\n\x0c\x66loat32array\x18\t \x01(\x0b\x32\x1b.straxrpc.Float32ArrayArrayH\x00\x12\x33\n\x0c\x66loat64array\x18\n \x01(\x0b\x32\x1b.straxrpc.Float64ArrayArrayH\x00\x12/\n\nint32array\x18\x0b \x01(\x0b\x32\x19.straxrpc.Int32ArrayArrayH\x00\x12/\n\nint64array\x18\x0c \x01(\x0b\x32\x19.straxrpc.Int64ArrayArrayH\x00\x42\x06\n\x04\x64\x61ta2\x82\x02\n\x08StraxRPC\x12@\n\x0bSearchField\x12\x17.straxrpc.SearchPattern\x1a\x14.straxrpc.ColumnInfo\"\x00\x30\x01\x12:\n\x08\x44\x61taInfo\x12\x14.straxrpc.PluginInfo\x1a\x14.straxrpc.DataColumn\"\x00\x30\x01\x12=\n\x0cGetDataframe\x12\x13.straxrpc.TableInfo\x1a\x14.straxrpc.DataColumn\"\x00\x30\x01\x12\x39\n\x08GetArray\x12\x13.straxrpc.TableInfo\x1a\x14.straxrpc.DataColumn\"\x00\x30\x01\x62\x06proto3')
)




_SEARCHPATTERN = _descriptor.Descriptor(
  name='SearchPattern',
  full_name='straxrpc.SearchPattern',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pattern', full_name='straxrpc.SearchPattern.pattern', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_matches', full_name='straxrpc.SearchPattern.max_matches', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=82,
)


_TABLEINFO = _descriptor.Descriptor(
  name='TableInfo',
  full_name='straxrpc.TableInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='straxrpc.TableInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run_id', full_name='straxrpc.TableInfo.run_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=125,
)


_PLUGININFO = _descriptor.Descriptor(
  name='PluginInfo',
  full_name='straxrpc.PluginInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='straxrpc.PluginInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='class_name', full_name='straxrpc.PluginInfo.class_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='straxrpc.PluginInfo.columns', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=212,
)


_COLUMNINFO = _descriptor.Descriptor(
  name='ColumnInfo',
  full_name='straxrpc.ColumnInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='straxrpc.ColumnInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_name', full_name='straxrpc.ColumnInfo.data_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plugin', full_name='straxrpc.ColumnInfo.plugin', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment', full_name='straxrpc.ColumnInfo.comment', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='straxrpc.ColumnInfo.dtype', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=214,
  serialized_end=307,
)


_INT32ARRAY = _descriptor.Descriptor(
  name='Int32Array',
  full_name='straxrpc.Int32Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='straxrpc.Int32Array.values', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=309,
  serialized_end=337,
)


_INT64ARRAY = _descriptor.Descriptor(
  name='Int64Array',
  full_name='straxrpc.Int64Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='straxrpc.Int64Array.values', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=339,
  serialized_end=367,
)


_INT32ARRAYARRAY = _descriptor.Descriptor(
  name='Int32ArrayArray',
  full_name='straxrpc.Int32ArrayArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='straxrpc.Int32ArrayArray.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=369,
  serialized_end=424,
)


_INT64ARRAYARRAY = _descriptor.Descriptor(
  name='Int64ArrayArray',
  full_name='straxrpc.Int64ArrayArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='straxrpc.Int64ArrayArray.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=426,
  serialized_end=481,
)


_BOOLARRAY = _descriptor.Descriptor(
  name='BoolArray',
  full_name='straxrpc.BoolArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='straxrpc.BoolArray.values', index=0,
      number=1, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=483,
  serialized_end=510,
)


_FLOAT32ARRAY = _descriptor.Descriptor(
  name='Float32Array',
  full_name='straxrpc.Float32Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='straxrpc.Float32Array.values', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=512,
  serialized_end=542,
)


_FLOAT64ARRAY = _descriptor.Descriptor(
  name='Float64Array',
  full_name='straxrpc.Float64Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='straxrpc.Float64Array.values', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=544,
  serialized_end=574,
)


_FLOAT32ARRAYARRAY = _descriptor.Descriptor(
  name='Float32ArrayArray',
  full_name='straxrpc.Float32ArrayArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='straxrpc.Float32ArrayArray.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=576,
  serialized_end=635,
)


_FLOAT64ARRAYARRAY = _descriptor.Descriptor(
  name='Float64ArrayArray',
  full_name='straxrpc.Float64ArrayArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='straxrpc.Float64ArrayArray.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=637,
  serialized_end=696,
)


_STRINGARRAY = _descriptor.Descriptor(
  name='StringArray',
  full_name='straxrpc.StringArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='straxrpc.StringArray.values', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=698,
  serialized_end=727,
)


_DATACOLUMN = _descriptor.Descriptor(
  name='DataColumn',
  full_name='straxrpc.DataColumn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='straxrpc.DataColumn.info', index=0,
      number=99, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='straxrpc.DataColumn.index', index=1,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int32', full_name='straxrpc.DataColumn.int32', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int64', full_name='straxrpc.DataColumn.int64', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float32', full_name='straxrpc.DataColumn.float32', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float64', full_name='straxrpc.DataColumn.float64', index=5,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string', full_name='straxrpc.DataColumn.string', index=6,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool', full_name='straxrpc.DataColumn.bool', index=7,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object', full_name='straxrpc.DataColumn.object', index=8,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float32array', full_name='straxrpc.DataColumn.float32array', index=9,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float64array', full_name='straxrpc.DataColumn.float64array', index=10,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int32array', full_name='straxrpc.DataColumn.int32array', index=11,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int64array', full_name='straxrpc.DataColumn.int64array', index=12,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='data', full_name='straxrpc.DataColumn.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=730,
  serialized_end=1288,
)

_PLUGININFO.fields_by_name['columns'].message_type = _COLUMNINFO
_INT32ARRAYARRAY.fields_by_name['values'].message_type = _INT32ARRAY
_INT64ARRAYARRAY.fields_by_name['values'].message_type = _INT64ARRAY
_FLOAT32ARRAYARRAY.fields_by_name['values'].message_type = _FLOAT32ARRAY
_FLOAT64ARRAYARRAY.fields_by_name['values'].message_type = _FLOAT64ARRAY
_DATACOLUMN.fields_by_name['info'].message_type = _COLUMNINFO
_DATACOLUMN.fields_by_name['int32'].message_type = _INT32ARRAY
_DATACOLUMN.fields_by_name['int64'].message_type = _INT64ARRAY
_DATACOLUMN.fields_by_name['float32'].message_type = _FLOAT32ARRAY
_DATACOLUMN.fields_by_name['float64'].message_type = _FLOAT64ARRAY
_DATACOLUMN.fields_by_name['string'].message_type = _STRINGARRAY
_DATACOLUMN.fields_by_name['bool'].message_type = _BOOLARRAY
_DATACOLUMN.fields_by_name['object'].message_type = _STRINGARRAY
_DATACOLUMN.fields_by_name['float32array'].message_type = _FLOAT32ARRAYARRAY
_DATACOLUMN.fields_by_name['float64array'].message_type = _FLOAT64ARRAYARRAY
_DATACOLUMN.fields_by_name['int32array'].message_type = _INT32ARRAYARRAY
_DATACOLUMN.fields_by_name['int64array'].message_type = _INT64ARRAYARRAY
_DATACOLUMN.oneofs_by_name['data'].fields.append(
  _DATACOLUMN.fields_by_name['int32'])
_DATACOLUMN.fields_by_name['int32'].containing_oneof = _DATACOLUMN.oneofs_by_name['data']
_DATACOLUMN.oneofs_by_name['data'].fields.append(
  _DATACOLUMN.fields_by_name['int64'])
_DATACOLUMN.fields_by_name['int64'].containing_oneof = _DATACOLUMN.oneofs_by_name['data']
_DATACOLUMN.oneofs_by_name['data'].fields.append(
  _DATACOLUMN.fields_by_name['float32'])
_DATACOLUMN.fields_by_name['float32'].containing_oneof = _DATACOLUMN.oneofs_by_name['data']
_DATACOLUMN.oneofs_by_name['data'].fields.append(
  _DATACOLUMN.fields_by_name['float64'])
_DATACOLUMN.fields_by_name['float64'].containing_oneof = _DATACOLUMN.oneofs_by_name['data']
_DATACOLUMN.oneofs_by_name['data'].fields.append(
  _DATACOLUMN.fields_by_name['string'])
_DATACOLUMN.fields_by_name['string'].containing_oneof = _DATACOLUMN.oneofs_by_name['data']
_DATACOLUMN.oneofs_by_name['data'].fields.append(
  _DATACOLUMN.fields_by_name['bool'])
_DATACOLUMN.fields_by_name['bool'].containing_oneof = _DATACOLUMN.oneofs_by_name['data']
_DATACOLUMN.oneofs_by_name['data'].fields.append(
  _DATACOLUMN.fields_by_name['object'])
_DATACOLUMN.fields_by_name['object'].containing_oneof = _DATACOLUMN.oneofs_by_name['data']
_DATACOLUMN.oneofs_by_name['data'].fields.append(
  _DATACOLUMN.fields_by_name['float32array'])
_DATACOLUMN.fields_by_name['float32array'].containing_oneof = _DATACOLUMN.oneofs_by_name['data']
_DATACOLUMN.oneofs_by_name['data'].fields.append(
  _DATACOLUMN.fields_by_name['float64array'])
_DATACOLUMN.fields_by_name['float64array'].containing_oneof = _DATACOLUMN.oneofs_by_name['data']
_DATACOLUMN.oneofs_by_name['data'].fields.append(
  _DATACOLUMN.fields_by_name['int32array'])
_DATACOLUMN.fields_by_name['int32array'].containing_oneof = _DATACOLUMN.oneofs_by_name['data']
_DATACOLUMN.oneofs_by_name['data'].fields.append(
  _DATACOLUMN.fields_by_name['int64array'])
_DATACOLUMN.fields_by_name['int64array'].containing_oneof = _DATACOLUMN.oneofs_by_name['data']
DESCRIPTOR.message_types_by_name['SearchPattern'] = _SEARCHPATTERN
DESCRIPTOR.message_types_by_name['TableInfo'] = _TABLEINFO
DESCRIPTOR.message_types_by_name['PluginInfo'] = _PLUGININFO
DESCRIPTOR.message_types_by_name['ColumnInfo'] = _COLUMNINFO
DESCRIPTOR.message_types_by_name['Int32Array'] = _INT32ARRAY
DESCRIPTOR.message_types_by_name['Int64Array'] = _INT64ARRAY
DESCRIPTOR.message_types_by_name['Int32ArrayArray'] = _INT32ARRAYARRAY
DESCRIPTOR.message_types_by_name['Int64ArrayArray'] = _INT64ARRAYARRAY
DESCRIPTOR.message_types_by_name['BoolArray'] = _BOOLARRAY
DESCRIPTOR.message_types_by_name['Float32Array'] = _FLOAT32ARRAY
DESCRIPTOR.message_types_by_name['Float64Array'] = _FLOAT64ARRAY
DESCRIPTOR.message_types_by_name['Float32ArrayArray'] = _FLOAT32ARRAYARRAY
DESCRIPTOR.message_types_by_name['Float64ArrayArray'] = _FLOAT64ARRAYARRAY
DESCRIPTOR.message_types_by_name['StringArray'] = _STRINGARRAY
DESCRIPTOR.message_types_by_name['DataColumn'] = _DATACOLUMN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchPattern = _reflection.GeneratedProtocolMessageType('SearchPattern', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHPATTERN,
  __module__ = 'strax_rpc_pb2'
  # @@protoc_insertion_point(class_scope:straxrpc.SearchPattern)
  ))
_sym_db.RegisterMessage(SearchPattern)

TableInfo = _reflection.GeneratedProtocolMessageType('TableInfo', (_message.Message,), dict(
  DESCRIPTOR = _TABLEINFO,
  __module__ = 'strax_rpc_pb2'
  # @@protoc_insertion_point(class_scope:straxrpc.TableInfo)
  ))
_sym_db.RegisterMessage(TableInfo)

PluginInfo = _reflection.GeneratedProtocolMessageType('PluginInfo', (_message.Message,), dict(
  DESCRIPTOR = _PLUGININFO,
  __module__ = 'strax_rpc_pb2'
  # @@protoc_insertion_point(class_scope:straxrpc.PluginInfo)
  ))
_sym_db.RegisterMessage(PluginInfo)

ColumnInfo = _reflection.GeneratedProtocolMessageType('ColumnInfo', (_message.Message,), dict(
  DESCRIPTOR = _COLUMNINFO,
  __module__ = 'strax_rpc_pb2'
  # @@protoc_insertion_point(class_scope:straxrpc.ColumnInfo)
  ))
_sym_db.RegisterMessage(ColumnInfo)

Int32Array = _reflection.GeneratedProtocolMessageType('Int32Array', (_message.Message,), dict(
  DESCRIPTOR = _INT32ARRAY,
  __module__ = 'strax_rpc_pb2'
  # @@protoc_insertion_point(class_scope:straxrpc.Int32Array)
  ))
_sym_db.RegisterMessage(Int32Array)

Int64Array = _reflection.GeneratedProtocolMessageType('Int64Array', (_message.Message,), dict(
  DESCRIPTOR = _INT64ARRAY,
  __module__ = 'strax_rpc_pb2'
  # @@protoc_insertion_point(class_scope:straxrpc.Int64Array)
  ))
_sym_db.RegisterMessage(Int64Array)

Int32ArrayArray = _reflection.GeneratedProtocolMessageType('Int32ArrayArray', (_message.Message,), dict(
  DESCRIPTOR = _INT32ARRAYARRAY,
  __module__ = 'strax_rpc_pb2'
  # @@protoc_insertion_point(class_scope:straxrpc.Int32ArrayArray)
  ))
_sym_db.RegisterMessage(Int32ArrayArray)

Int64ArrayArray = _reflection.GeneratedProtocolMessageType('Int64ArrayArray', (_message.Message,), dict(
  DESCRIPTOR = _INT64ARRAYARRAY,
  __module__ = 'strax_rpc_pb2'
  # @@protoc_insertion_point(class_scope:straxrpc.Int64ArrayArray)
  ))
_sym_db.RegisterMessage(Int64ArrayArray)

BoolArray = _reflection.GeneratedProtocolMessageType('BoolArray', (_message.Message,), dict(
  DESCRIPTOR = _BOOLARRAY,
  __module__ = 'strax_rpc_pb2'
  # @@protoc_insertion_point(class_scope:straxrpc.BoolArray)
  ))
_sym_db.RegisterMessage(BoolArray)

Float32Array = _reflection.GeneratedProtocolMessageType('Float32Array', (_message.Message,), dict(
  DESCRIPTOR = _FLOAT32ARRAY,
  __module__ = 'strax_rpc_pb2'
  # @@protoc_insertion_point(class_scope:straxrpc.Float32Array)
  ))
_sym_db.RegisterMessage(Float32Array)

Float64Array = _reflection.GeneratedProtocolMessageType('Float64Array', (_message.Message,), dict(
  DESCRIPTOR = _FLOAT64ARRAY,
  __module__ = 'strax_rpc_pb2'
  # @@protoc_insertion_point(class_scope:straxrpc.Float64Array)
  ))
_sym_db.RegisterMessage(Float64Array)

Float32ArrayArray = _reflection.GeneratedProtocolMessageType('Float32ArrayArray', (_message.Message,), dict(
  DESCRIPTOR = _FLOAT32ARRAYARRAY,
  __module__ = 'strax_rpc_pb2'
  # @@protoc_insertion_point(class_scope:straxrpc.Float32ArrayArray)
  ))
_sym_db.RegisterMessage(Float32ArrayArray)

Float64ArrayArray = _reflection.GeneratedProtocolMessageType('Float64ArrayArray', (_message.Message,), dict(
  DESCRIPTOR = _FLOAT64ARRAYARRAY,
  __module__ = 'strax_rpc_pb2'
  # @@protoc_insertion_point(class_scope:straxrpc.Float64ArrayArray)
  ))
_sym_db.RegisterMessage(Float64ArrayArray)

StringArray = _reflection.GeneratedProtocolMessageType('StringArray', (_message.Message,), dict(
  DESCRIPTOR = _STRINGARRAY,
  __module__ = 'strax_rpc_pb2'
  # @@protoc_insertion_point(class_scope:straxrpc.StringArray)
  ))
_sym_db.RegisterMessage(StringArray)

DataColumn = _reflection.GeneratedProtocolMessageType('DataColumn', (_message.Message,), dict(
  DESCRIPTOR = _DATACOLUMN,
  __module__ = 'strax_rpc_pb2'
  # @@protoc_insertion_point(class_scope:straxrpc.DataColumn)
  ))
_sym_db.RegisterMessage(DataColumn)



_STRAXRPC = _descriptor.ServiceDescriptor(
  name='StraxRPC',
  full_name='straxrpc.StraxRPC',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1291,
  serialized_end=1549,
  methods=[
  _descriptor.MethodDescriptor(
    name='SearchField',
    full_name='straxrpc.StraxRPC.SearchField',
    index=0,
    containing_service=None,
    input_type=_SEARCHPATTERN,
    output_type=_COLUMNINFO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DataInfo',
    full_name='straxrpc.StraxRPC.DataInfo',
    index=1,
    containing_service=None,
    input_type=_PLUGININFO,
    output_type=_DATACOLUMN,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetDataframe',
    full_name='straxrpc.StraxRPC.GetDataframe',
    index=2,
    containing_service=None,
    input_type=_TABLEINFO,
    output_type=_DATACOLUMN,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetArray',
    full_name='straxrpc.StraxRPC.GetArray',
    index=3,
    containing_service=None,
    input_type=_TABLEINFO,
    output_type=_DATACOLUMN,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STRAXRPC)

DESCRIPTOR.services_by_name['StraxRPC'] = _STRAXRPC

# @@protoc_insertion_point(module_scope)