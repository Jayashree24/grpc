# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: primenumber.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='primenumber.proto',
  package='calculator',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11primenumber.proto\x12\ncalculator\"\x1b\n\x0cPrimeRequest\x12\x0b\n\x03num\x18\x01 \x01(\x05\"\x1c\n\nPrimeReply\x12\x0e\n\x06\x66\x61\x63tor\x18\x01 \x01(\x05\x32Y\n\x12PrimeDecomposition\x12\x43\n\x0bPrimeNumber\x12\x18.calculator.PrimeRequest\x1a\x16.calculator.PrimeReply\"\x00\x30\x01\x62\x06proto3'
)




_PRIMEREQUEST = _descriptor.Descriptor(
  name='PrimeRequest',
  full_name='calculator.PrimeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='calculator.PrimeRequest.num', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=60,
)


_PRIMEREPLY = _descriptor.Descriptor(
  name='PrimeReply',
  full_name='calculator.PrimeReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='factor', full_name='calculator.PrimeReply.factor', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=90,
)

DESCRIPTOR.message_types_by_name['PrimeRequest'] = _PRIMEREQUEST
DESCRIPTOR.message_types_by_name['PrimeReply'] = _PRIMEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PrimeRequest = _reflection.GeneratedProtocolMessageType('PrimeRequest', (_message.Message,), {
  'DESCRIPTOR' : _PRIMEREQUEST,
  '__module__' : 'primenumber_pb2'
  # @@protoc_insertion_point(class_scope:calculator.PrimeRequest)
  })
_sym_db.RegisterMessage(PrimeRequest)

PrimeReply = _reflection.GeneratedProtocolMessageType('PrimeReply', (_message.Message,), {
  'DESCRIPTOR' : _PRIMEREPLY,
  '__module__' : 'primenumber_pb2'
  # @@protoc_insertion_point(class_scope:calculator.PrimeReply)
  })
_sym_db.RegisterMessage(PrimeReply)



_PRIMEDECOMPOSITION = _descriptor.ServiceDescriptor(
  name='PrimeDecomposition',
  full_name='calculator.PrimeDecomposition',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=92,
  serialized_end=181,
  methods=[
  _descriptor.MethodDescriptor(
    name='PrimeNumber',
    full_name='calculator.PrimeDecomposition.PrimeNumber',
    index=0,
    containing_service=None,
    input_type=_PRIMEREQUEST,
    output_type=_PRIMEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PRIMEDECOMPOSITION)

DESCRIPTOR.services_by_name['PrimeDecomposition'] = _PRIMEDECOMPOSITION

# @@protoc_insertion_point(module_scope)
