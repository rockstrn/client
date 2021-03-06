# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='websearch2/proto/news_recommendation/gcd_user_profile.proto',
  package='GcdUserProfile',
  serialized_pb='\n;websearch2/proto/news_recommendation/gcd_user_profile.proto\x12\x0eGcdUserProfile\"q\n\x15GcdUserProfileReadReq\x12\x10\n\x08req_type\x18\x01 \x01(\r\x12\x11\n\tdevice_id\x18\x02 \x01(\x0c\x12\x0e\n\x03uin\x18\x03 \x01(\x04:\x01\x30\x12\x10\n\x08platform\x18\x04 \x01(\r\x12\x11\n\tsignature\x18\x05 \x01(\x0c\"-\n\x0bGameTagInfo\x12\x0e\n\x06tag_id\x18\x01 \x01(\x0c\x12\x0e\n\x06weight\x18\x02 \x01(\x02\"\x8c\x01\n\x15GcdUserProfileReadRsp\x12\x11\n\tdevice_id\x18\x01 \x01(\x0c\x12\x0b\n\x03uin\x18\x02 \x01(\x04\x12\x32\n\rgame_tag_info\x18\x03 \x03(\x0b\x32\x1b.GcdUserProfile.GameTagInfo\x12\x0e\n\x06\x65rr_no\x18\x04 \x01(\x05\x12\x0f\n\x07\x65rr_msg\x18\x05 \x01(\x0c')




_GCDUSERPROFILEREADREQ = descriptor.Descriptor(
  name='GcdUserProfileReadReq',
  full_name='GcdUserProfile.GcdUserProfileReadReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='req_type', full_name='GcdUserProfile.GcdUserProfileReadReq.req_type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='device_id', full_name='GcdUserProfile.GcdUserProfileReadReq.device_id', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='uin', full_name='GcdUserProfile.GcdUserProfileReadReq.uin', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='platform', full_name='GcdUserProfile.GcdUserProfileReadReq.platform', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='signature', full_name='GcdUserProfile.GcdUserProfileReadReq.signature', index=4,
      number=5, type=12, cpp_type=9, label=1,
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
  serialized_start=79,
  serialized_end=192,
)


_GAMETAGINFO = descriptor.Descriptor(
  name='GameTagInfo',
  full_name='GcdUserProfile.GameTagInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='tag_id', full_name='GcdUserProfile.GameTagInfo.tag_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='weight', full_name='GcdUserProfile.GameTagInfo.weight', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=194,
  serialized_end=239,
)


_GCDUSERPROFILEREADRSP = descriptor.Descriptor(
  name='GcdUserProfileReadRsp',
  full_name='GcdUserProfile.GcdUserProfileReadRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='device_id', full_name='GcdUserProfile.GcdUserProfileReadRsp.device_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='uin', full_name='GcdUserProfile.GcdUserProfileReadRsp.uin', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='game_tag_info', full_name='GcdUserProfile.GcdUserProfileReadRsp.game_tag_info', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='err_no', full_name='GcdUserProfile.GcdUserProfileReadRsp.err_no', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='err_msg', full_name='GcdUserProfile.GcdUserProfileReadRsp.err_msg', index=4,
      number=5, type=12, cpp_type=9, label=1,
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
  serialized_start=242,
  serialized_end=382,
)


_GCDUSERPROFILEREADRSP.fields_by_name['game_tag_info'].message_type = _GAMETAGINFO

class GcdUserProfileReadReq(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GCDUSERPROFILEREADREQ
  
  # @@protoc_insertion_point(class_scope:GcdUserProfile.GcdUserProfileReadReq)

class GameTagInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GAMETAGINFO
  
  # @@protoc_insertion_point(class_scope:GcdUserProfile.GameTagInfo)

class GcdUserProfileReadRsp(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GCDUSERPROFILEREADRSP
  
  # @@protoc_insertion_point(class_scope:GcdUserProfile.GcdUserProfileReadRsp)

# @@protoc_insertion_point(module_scope)
