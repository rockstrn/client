# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='websearch2/proto/news_recommendation/rcm_queue/rcm_queue_root_diagnosis_common.proto',
  package='pb.rcm.queue.video.diagnosis',
  serialized_pb='\nTwebsearch2/proto/news_recommendation/rcm_queue/rcm_queue_root_diagnosis_common.proto\x12\x1cpb.rcm.queue.video.diagnosis\"\'\n\textra_mes\x12\x0b\n\x03key\x18\x01 \x02(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\"\xde\x01\n\nServerStat\x12\x13\n\x0bserver_name\x18\x01 \x01(\x0c\x12\x11\n\tserver_ip\x18\x02 \x01(\t\x12\x13\n\x0bserver_port\x18\x03 \x01(\r\x12\x16\n\x0btimecost_ms\x18\x04 \x01(\r:\x01\x30\x12\x12\n\ntimeout_ms\x18\x05 \x01(\r\x12\x14\n\x0cnet_ret_code\x18\x06 \x01(\x03\x12\x14\n\x0csvr_ret_code\x18\x07 \x01(\x03\x12;\n\nextra_info\x18\x08 \x03(\x0b\x32\'.pb.rcm.queue.video.diagnosis.extra_mes\"\x85\x04\n\x0e\x44iagnosisFlags\x12Q\n\x0bportrait_en\x18\x01 \x01(\x0e\x32-.pb.rcm.queue.video.diagnosis.DiagnosisSwitch:\rDIAGNOSIS_OFF\x12O\n\trecall_en\x18\x02 \x01(\x0e\x32-.pb.rcm.queue.video.diagnosis.DiagnosisSwitch:\rDIAGNOSIS_OFF\x12N\n\x08score_en\x18\x03 \x01(\x0e\x32-.pb.rcm.queue.video.diagnosis.DiagnosisSwitch:\rDIAGNOSIS_OFF\x12Q\n\x0bstrategy_en\x18\x04 \x01(\x0e\x32-.pb.rcm.queue.video.diagnosis.DiagnosisSwitch:\rDIAGNOSIS_OFF\x12W\n\x11new_user_video_en\x18\x05 \x01(\x0e\x32-.pb.rcm.queue.video.diagnosis.DiagnosisSwitch:\rDIAGNOSIS_OFF\x12S\n\rrecall_log_en\x18\x06 \x01(\x0e\x32-.pb.rcm.queue.video.diagnosis.DiagnosisSwitch:\rDIAGNOSIS_OFF*h\n\x0f\x44iagnosisSwitch\x12\x11\n\rDIAGNOSIS_OFF\x10\x00\x12\x16\n\x12\x44IAGNOSIS_REQ_ONLY\x10\x01\x12\x16\n\x12\x44IAGNOSIS_RSP_ONLY\x10\x02\x12\x12\n\x0e\x44IAGNOSIS_BOTH\x10\x03')

_DIAGNOSISSWITCH = descriptor.EnumDescriptor(
  name='DiagnosisSwitch',
  full_name='pb.rcm.queue.video.diagnosis.DiagnosisSwitch',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='DIAGNOSIS_OFF', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DIAGNOSIS_REQ_ONLY', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DIAGNOSIS_RSP_ONLY', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DIAGNOSIS_BOTH', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=904,
  serialized_end=1008,
)


DIAGNOSIS_OFF = 0
DIAGNOSIS_REQ_ONLY = 1
DIAGNOSIS_RSP_ONLY = 2
DIAGNOSIS_BOTH = 3



_EXTRA_MES = descriptor.Descriptor(
  name='extra_mes',
  full_name='pb.rcm.queue.video.diagnosis.extra_mes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='key', full_name='pb.rcm.queue.video.diagnosis.extra_mes.key', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='pb.rcm.queue.video.diagnosis.extra_mes.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  is_extendable=False,
  extension_ranges=[],
  serialized_start=118,
  serialized_end=157,
)


_SERVERSTAT = descriptor.Descriptor(
  name='ServerStat',
  full_name='pb.rcm.queue.video.diagnosis.ServerStat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='server_name', full_name='pb.rcm.queue.video.diagnosis.ServerStat.server_name', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='server_ip', full_name='pb.rcm.queue.video.diagnosis.ServerStat.server_ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='server_port', full_name='pb.rcm.queue.video.diagnosis.ServerStat.server_port', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timecost_ms', full_name='pb.rcm.queue.video.diagnosis.ServerStat.timecost_ms', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timeout_ms', full_name='pb.rcm.queue.video.diagnosis.ServerStat.timeout_ms', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='net_ret_code', full_name='pb.rcm.queue.video.diagnosis.ServerStat.net_ret_code', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='svr_ret_code', full_name='pb.rcm.queue.video.diagnosis.ServerStat.svr_ret_code', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extra_info', full_name='pb.rcm.queue.video.diagnosis.ServerStat.extra_info', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  is_extendable=False,
  extension_ranges=[],
  serialized_start=160,
  serialized_end=382,
)


_DIAGNOSISFLAGS = descriptor.Descriptor(
  name='DiagnosisFlags',
  full_name='pb.rcm.queue.video.diagnosis.DiagnosisFlags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='portrait_en', full_name='pb.rcm.queue.video.diagnosis.DiagnosisFlags.portrait_en', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='recall_en', full_name='pb.rcm.queue.video.diagnosis.DiagnosisFlags.recall_en', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='score_en', full_name='pb.rcm.queue.video.diagnosis.DiagnosisFlags.score_en', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='strategy_en', full_name='pb.rcm.queue.video.diagnosis.DiagnosisFlags.strategy_en', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='new_user_video_en', full_name='pb.rcm.queue.video.diagnosis.DiagnosisFlags.new_user_video_en', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='recall_log_en', full_name='pb.rcm.queue.video.diagnosis.DiagnosisFlags.recall_log_en', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
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
  is_extendable=False,
  extension_ranges=[],
  serialized_start=385,
  serialized_end=902,
)


_SERVERSTAT.fields_by_name['extra_info'].message_type = _EXTRA_MES
_DIAGNOSISFLAGS.fields_by_name['portrait_en'].enum_type = _DIAGNOSISSWITCH
_DIAGNOSISFLAGS.fields_by_name['recall_en'].enum_type = _DIAGNOSISSWITCH
_DIAGNOSISFLAGS.fields_by_name['score_en'].enum_type = _DIAGNOSISSWITCH
_DIAGNOSISFLAGS.fields_by_name['strategy_en'].enum_type = _DIAGNOSISSWITCH
_DIAGNOSISFLAGS.fields_by_name['new_user_video_en'].enum_type = _DIAGNOSISSWITCH
_DIAGNOSISFLAGS.fields_by_name['recall_log_en'].enum_type = _DIAGNOSISSWITCH

class extra_mes(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXTRA_MES
  
  # @@protoc_insertion_point(class_scope:pb.rcm.queue.video.diagnosis.extra_mes)

class ServerStat(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SERVERSTAT
  
  # @@protoc_insertion_point(class_scope:pb.rcm.queue.video.diagnosis.ServerStat)

class DiagnosisFlags(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DIAGNOSISFLAGS
  
  # @@protoc_insertion_point(class_scope:pb.rcm.queue.video.diagnosis.DiagnosisFlags)

# @@protoc_insertion_point(module_scope)