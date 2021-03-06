# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='websearch2/proto/news_recommendation/rcm_queue/rcm_queue_log.proto',
  package='pb.rcm.queue',
  serialized_pb='\nBwebsearch2/proto/news_recommendation/rcm_queue/rcm_queue_log.proto\x12\x0cpb.rcm.queue\x1a>websearch2/proto/news_recommendation/rcm_queue/rcm_queue.proto\"\x97\x01\n\x07ShowLog\x12\"\n\x03req\x18\x01 \x01(\x0b\x32\x15.pb.rcm.queue.Request\x12#\n\x03rsp\x18\x02 \x01(\x0b\x32\x16.pb.rcm.queue.Response\x12\x12\n\ntime_stamp\x18\x03 \x02(\r\x12\x11\n\tserver_ip\x18\x04 \x01(\t\x12\x11\n\tclient_ip\x18\x05 \x01(\t*\t\x08\x90N\x10\x80\x80\x80\x80\x02')




_SHOWLOG = descriptor.Descriptor(
  name='ShowLog',
  full_name='pb.rcm.queue.ShowLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='req', full_name='pb.rcm.queue.ShowLog.req', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rsp', full_name='pb.rcm.queue.ShowLog.rsp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='time_stamp', full_name='pb.rcm.queue.ShowLog.time_stamp', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='server_ip', full_name='pb.rcm.queue.ShowLog.server_ip', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='client_ip', full_name='pb.rcm.queue.ShowLog.client_ip', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(10000, 536870912), ],
  serialized_start=149,
  serialized_end=300,
)

import websearch2.proto.news_recommendation.rcm_queue.rcm_queue_pb2

_SHOWLOG.fields_by_name['req'].message_type = websearch2.proto.news_recommendation.rcm_queue.rcm_queue_pb2._REQUEST
_SHOWLOG.fields_by_name['rsp'].message_type = websearch2.proto.news_recommendation.rcm_queue.rcm_queue_pb2._RESPONSE

class ShowLog(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SHOWLOG
  
  # @@protoc_insertion_point(class_scope:pb.rcm.queue.ShowLog)

# @@protoc_insertion_point(module_scope)
