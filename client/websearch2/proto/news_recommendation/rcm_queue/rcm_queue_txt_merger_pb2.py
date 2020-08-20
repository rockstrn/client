# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='websearch2/proto/news_recommendation/rcm_queue/rcm_queue_txt_merger.proto',
  package='pb.rcm.queue.txt',
  serialized_pb='\nIwebsearch2/proto/news_recommendation/rcm_queue/rcm_queue_txt_merger.proto\x12\x10pb.rcm.queue.txt\x1a\x42websearch2/proto/news_recommendation/rcm_queue/rcm_queue_req.proto\x1a\x42websearch2/proto/news_recommendation/rcm_queue/rcm_queue_rsp.proto\x1a\x42websearch2/proto/news_recommendation/rcm_queue/rcm_queue_txt.proto\x1a>websearch2/proto/news_recommendation/rcm_queue/rcm_queue.proto\x1a\x42websearch2/proto/news_recommendation/guanxin_news_rcm_common.proto\"\x9b\x02\n\x10TxtMergerRequest\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\x0c\x12\x10\n\x08\x61lg_type\x18\x02 \x02(\x0c\x12\x11\n\talg_extra\x18\x03 \x01(\x0c\x12>\n\x11human_refine_docs\x18\x04 \x03(\x0b\x32#.pb.guanxin.news_rcm.HumanRefineDoc\x12\x13\n\x0b\x61lg_version\x18\x06 \x01(\r\x12\x10\n\x08trace_id\x18\x07 \x01(\x0c\x12\x15\n\ndebug_flag\x18\x64 \x01(\x04:\x01\x30\x12\x18\n\rdegrade_level\x18\x65 \x01(\r:\x01\x30\x12)\n\x07req_ext\x18\x66 \x01(\x0b\x32\x18.pb.rcm.queue.txt.ReqExt\x12\x0e\n\x06omg_id\x18g \x01(\x0c\"\xab\x03\n\x11TxtMergerUserInfo\x12\x10\n\x08\x63hl_from\x18\x01 \x01(\x0c\x12\x12\n\nitem_count\x18\x02 \x01(\x04\x12\x0c\n\x04luin\x18\x03 \x01(\x0c\x12\r\n\x05lskey\x18\x04 \x01(\x0c\x12\x1d\n\x0ehas_user_model\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x11\n\thome_town\x18\x06 \x01(\x0c\x12\x0c\n\x04imsi\x18\x07 \x01(\x0c\x12\x12\n\nudevice_id\x18\x08 \x01(\x0c\x12\x10\n\x08\x63urr_loc\x18\t \x01(\x0c\x12\"\n\x13has_ckv_topic_model\x18\n \x01(\x08:\x05\x66\x61lse\x12\x33\n\x0cuser_profile\x18\x0b \x01(\x0b\x32\x1d.pb.rcm.queue.txt.UserProfile\x12\x34\n\ntx_lbs_loc\x18\x0c \x01(\x0b\x32 .pb.rcm.queue.txt.TxLocationInfo\x12\x12\n\ngender_val\x18\r \x01(\r\x12\x18\n\x10usermodel_source\x18\x0e \x01(\r\x12\x16\n\x0eusermodel_flag\x18\x0f \x01(\x05\x12\x18\n\x10userlogin_source\x18\x10 \x01(\r\"\xdc\x01\n\x10TxtMergerReqArgs\x12\x1b\n\x0cis_retry_req\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x31\n\trdm_debug\x18\x02 \x03(\x0b\x32\x1e.pb.rcm.queue.txt.RDMDebugInfo\x12\x14\n\tdoc_level\x18\n \x01(\x05:\x01\x31\x12\x17\n\x0c\x66ilter_value\x18\x0b \x01(\x05:\x01\x30\x12\x17\n\x08no_trace\x18\x0c \x01(\x08:\x05\x66\x61lse\x12\x30\n\nreq_source\x18\r \x01(\x0e\x32\x1c.pb.rcm.queue.txt.EReqSource\"1\n\x07\x43\x46Seeds\x12\x10\n\x08src_docs\x18\x01 \x02(\x0c\x12\x14\n\x0c\x63\x66_seed_docs\x18\x02 \x03(\x04\"\xb5\x03\n\x11TxtMergerResponse\x12$\n\x04user\x18\x01 \x02(\x0b\x32\x16.pb.rcm.queue.UserInfo\x12\x12\n\nalg_status\x18\x02 \x02(\r\x12\x15\n\rrecomm_reason\x18\x03 \x01(\x0c\x12\x13\n\x0b\x61lg_version\x18\x04 \x02(\r\x12\x0e\n\x06seq_no\x18\x05 \x02(\x0c\x12\x16\n\x0e\x65xp_ir_doc_num\x18\x06 \x01(\r\x12\x16\n\x0erel_ir_doc_num\x18\x07 \x01(\r\x12\x10\n\x08trace_id\x18\x08 \x01(\x0c\x12\x13\n\x0brecall_info\x18\t \x01(\x0c\x12+\n\x08\x63\x66_seeds\x18\n \x03(\x0b\x32\x19.pb.rcm.queue.txt.CFSeeds\x12\x19\n\x11is_set_con_filter\x18\x0b \x01(\x08\x12\x11\n\tdiag_info\x18g \x01(\x0c\x12)\n\x07rsp_ext\x18h \x01(\x0b\x32\x18.pb.rcm.queue.txt.RspExt\x12\x18\n\x10\x66resh_debug_info\x18i \x01(\x0c\x12\x18\n\x10video_debug_info\x18j \x01(\x0c\x12\x19\n\x11video_recall_info\x18k \x01(\x0c\"\xfb\x01\n\x17TxtMergerServerResponse\x12-\n\x02rc\x18\x01 \x02(\x0e\x32\x18.pb.rcm.queue.ReturnCode:\x07\x45_RC_OK\x12\x11\n\ttime_cost\x18\x02 \x01(\r\x12\x16\n\x0b\x64\x61ta_source\x18\x03 \x01(\x05:\x01\x30\x12\x39\n\rstrategy_info\x18\x04 \x03(\x0b\x32\".pb.guanxin.news_rcm.StrategyTrack\x12\x12\n\ndebug_info\x18\x05 \x01(\x0c\x12,\n\x0brsp_ext_new\x18\x07 \x01(\x0b\x32\x17.pb.rcm.queue.RspExtNew*\t\x08\x90N\x10\x80\x80\x80\x80\x02:R\n\x0etxt_merger_req\x12\x15.pb.rcm.queue.Request\x18\xa5N \x01(\x0b\x32\".pb.rcm.queue.txt.TxtMergerRequest:U\n\x0ftxt_merger_user\x12\x16.pb.rcm.queue.UserInfo\x18\xa5N \x01(\x0b\x32#.pb.rcm.queue.txt.TxtMergerUserInfo:W\n\x13txt_merger_req_args\x12\x15.pb.rcm.queue.ReqArgs\x18\xa5N \x01(\x0b\x32\".pb.rcm.queue.txt.TxtMergerReqArgs:T\n\x0etxt_merger_rsp\x12\x16.pb.rcm.queue.Response\x18\xa5N \x01(\x0b\x32#.pb.rcm.queue.txt.TxtMergerResponse')


TXT_MERGER_REQ_FIELD_NUMBER = 10021
txt_merger_req = descriptor.FieldDescriptor(
  name='txt_merger_req', full_name='pb.rcm.queue.txt.txt_merger_req', index=0,
  number=10021, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
TXT_MERGER_USER_FIELD_NUMBER = 10021
txt_merger_user = descriptor.FieldDescriptor(
  name='txt_merger_user', full_name='pb.rcm.queue.txt.txt_merger_user', index=1,
  number=10021, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
TXT_MERGER_REQ_ARGS_FIELD_NUMBER = 10021
txt_merger_req_args = descriptor.FieldDescriptor(
  name='txt_merger_req_args', full_name='pb.rcm.queue.txt.txt_merger_req_args', index=2,
  number=10021, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
TXT_MERGER_RSP_FIELD_NUMBER = 10021
txt_merger_rsp = descriptor.FieldDescriptor(
  name='txt_merger_rsp', full_name='pb.rcm.queue.txt.txt_merger_rsp', index=3,
  number=10021, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_TXTMERGERREQUEST = descriptor.Descriptor(
  name='TxtMergerRequest',
  full_name='pb.rcm.queue.txt.TxtMergerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='channel', full_name='pb.rcm.queue.txt.TxtMergerRequest.channel', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='alg_type', full_name='pb.rcm.queue.txt.TxtMergerRequest.alg_type', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='alg_extra', full_name='pb.rcm.queue.txt.TxtMergerRequest.alg_extra', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='human_refine_docs', full_name='pb.rcm.queue.txt.TxtMergerRequest.human_refine_docs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='alg_version', full_name='pb.rcm.queue.txt.TxtMergerRequest.alg_version', index=4,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='trace_id', full_name='pb.rcm.queue.txt.TxtMergerRequest.trace_id', index=5,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='debug_flag', full_name='pb.rcm.queue.txt.TxtMergerRequest.debug_flag', index=6,
      number=100, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='degrade_level', full_name='pb.rcm.queue.txt.TxtMergerRequest.degrade_level', index=7,
      number=101, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='req_ext', full_name='pb.rcm.queue.txt.TxtMergerRequest.req_ext', index=8,
      number=102, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='omg_id', full_name='pb.rcm.queue.txt.TxtMergerRequest.omg_id', index=9,
      number=103, type=12, cpp_type=9, label=1,
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
  serialized_start=432,
  serialized_end=715,
)


_TXTMERGERUSERINFO = descriptor.Descriptor(
  name='TxtMergerUserInfo',
  full_name='pb.rcm.queue.txt.TxtMergerUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='chl_from', full_name='pb.rcm.queue.txt.TxtMergerUserInfo.chl_from', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='item_count', full_name='pb.rcm.queue.txt.TxtMergerUserInfo.item_count', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='luin', full_name='pb.rcm.queue.txt.TxtMergerUserInfo.luin', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lskey', full_name='pb.rcm.queue.txt.TxtMergerUserInfo.lskey', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='has_user_model', full_name='pb.rcm.queue.txt.TxtMergerUserInfo.has_user_model', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='home_town', full_name='pb.rcm.queue.txt.TxtMergerUserInfo.home_town', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='imsi', full_name='pb.rcm.queue.txt.TxtMergerUserInfo.imsi', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='udevice_id', full_name='pb.rcm.queue.txt.TxtMergerUserInfo.udevice_id', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='curr_loc', full_name='pb.rcm.queue.txt.TxtMergerUserInfo.curr_loc', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='has_ckv_topic_model', full_name='pb.rcm.queue.txt.TxtMergerUserInfo.has_ckv_topic_model', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_profile', full_name='pb.rcm.queue.txt.TxtMergerUserInfo.user_profile', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tx_lbs_loc', full_name='pb.rcm.queue.txt.TxtMergerUserInfo.tx_lbs_loc', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='gender_val', full_name='pb.rcm.queue.txt.TxtMergerUserInfo.gender_val', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='usermodel_source', full_name='pb.rcm.queue.txt.TxtMergerUserInfo.usermodel_source', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='usermodel_flag', full_name='pb.rcm.queue.txt.TxtMergerUserInfo.usermodel_flag', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='userlogin_source', full_name='pb.rcm.queue.txt.TxtMergerUserInfo.userlogin_source', index=15,
      number=16, type=13, cpp_type=3, label=1,
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
  serialized_start=718,
  serialized_end=1145,
)


_TXTMERGERREQARGS = descriptor.Descriptor(
  name='TxtMergerReqArgs',
  full_name='pb.rcm.queue.txt.TxtMergerReqArgs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='is_retry_req', full_name='pb.rcm.queue.txt.TxtMergerReqArgs.is_retry_req', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rdm_debug', full_name='pb.rcm.queue.txt.TxtMergerReqArgs.rdm_debug', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='doc_level', full_name='pb.rcm.queue.txt.TxtMergerReqArgs.doc_level', index=2,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='filter_value', full_name='pb.rcm.queue.txt.TxtMergerReqArgs.filter_value', index=3,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='no_trace', full_name='pb.rcm.queue.txt.TxtMergerReqArgs.no_trace', index=4,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='req_source', full_name='pb.rcm.queue.txt.TxtMergerReqArgs.req_source', index=5,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
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
  serialized_start=1148,
  serialized_end=1368,
)


_CFSEEDS = descriptor.Descriptor(
  name='CFSeeds',
  full_name='pb.rcm.queue.txt.CFSeeds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='src_docs', full_name='pb.rcm.queue.txt.CFSeeds.src_docs', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cf_seed_docs', full_name='pb.rcm.queue.txt.CFSeeds.cf_seed_docs', index=1,
      number=2, type=4, cpp_type=4, label=3,
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
  serialized_start=1370,
  serialized_end=1419,
)


_TXTMERGERRESPONSE = descriptor.Descriptor(
  name='TxtMergerResponse',
  full_name='pb.rcm.queue.txt.TxtMergerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='user', full_name='pb.rcm.queue.txt.TxtMergerResponse.user', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='alg_status', full_name='pb.rcm.queue.txt.TxtMergerResponse.alg_status', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='recomm_reason', full_name='pb.rcm.queue.txt.TxtMergerResponse.recomm_reason', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='alg_version', full_name='pb.rcm.queue.txt.TxtMergerResponse.alg_version', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='seq_no', full_name='pb.rcm.queue.txt.TxtMergerResponse.seq_no', index=4,
      number=5, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='exp_ir_doc_num', full_name='pb.rcm.queue.txt.TxtMergerResponse.exp_ir_doc_num', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rel_ir_doc_num', full_name='pb.rcm.queue.txt.TxtMergerResponse.rel_ir_doc_num', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='trace_id', full_name='pb.rcm.queue.txt.TxtMergerResponse.trace_id', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='recall_info', full_name='pb.rcm.queue.txt.TxtMergerResponse.recall_info', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cf_seeds', full_name='pb.rcm.queue.txt.TxtMergerResponse.cf_seeds', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_set_con_filter', full_name='pb.rcm.queue.txt.TxtMergerResponse.is_set_con_filter', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='diag_info', full_name='pb.rcm.queue.txt.TxtMergerResponse.diag_info', index=11,
      number=103, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rsp_ext', full_name='pb.rcm.queue.txt.TxtMergerResponse.rsp_ext', index=12,
      number=104, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='fresh_debug_info', full_name='pb.rcm.queue.txt.TxtMergerResponse.fresh_debug_info', index=13,
      number=105, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='video_debug_info', full_name='pb.rcm.queue.txt.TxtMergerResponse.video_debug_info', index=14,
      number=106, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='video_recall_info', full_name='pb.rcm.queue.txt.TxtMergerResponse.video_recall_info', index=15,
      number=107, type=12, cpp_type=9, label=1,
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
  serialized_start=1422,
  serialized_end=1859,
)


_TXTMERGERSERVERRESPONSE = descriptor.Descriptor(
  name='TxtMergerServerResponse',
  full_name='pb.rcm.queue.txt.TxtMergerServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='rc', full_name='pb.rcm.queue.txt.TxtMergerServerResponse.rc', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='time_cost', full_name='pb.rcm.queue.txt.TxtMergerServerResponse.time_cost', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_source', full_name='pb.rcm.queue.txt.TxtMergerServerResponse.data_source', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='strategy_info', full_name='pb.rcm.queue.txt.TxtMergerServerResponse.strategy_info', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='debug_info', full_name='pb.rcm.queue.txt.TxtMergerServerResponse.debug_info', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rsp_ext_new', full_name='pb.rcm.queue.txt.TxtMergerServerResponse.rsp_ext_new', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1862,
  serialized_end=2113,
)

import websearch2.proto.news_recommendation.rcm_queue.rcm_queue_req_pb2
import websearch2.proto.news_recommendation.rcm_queue.rcm_queue_rsp_pb2
import websearch2.proto.news_recommendation.rcm_queue.rcm_queue_txt_pb2
import websearch2.proto.news_recommendation.rcm_queue.rcm_queue_pb2
import websearch2.proto.news_recommendation.guanxin_news_rcm_common_pb2

_TXTMERGERREQUEST.fields_by_name['human_refine_docs'].message_type = websearch2.proto.news_recommendation.guanxin_news_rcm_common_pb2._HUMANREFINEDOC
_TXTMERGERREQUEST.fields_by_name['req_ext'].message_type = websearch2.proto.news_recommendation.rcm_queue.rcm_queue_txt_pb2._REQEXT
_TXTMERGERUSERINFO.fields_by_name['user_profile'].message_type = websearch2.proto.news_recommendation.rcm_queue.rcm_queue_txt_pb2._USERPROFILE
_TXTMERGERUSERINFO.fields_by_name['tx_lbs_loc'].message_type = websearch2.proto.news_recommendation.rcm_queue.rcm_queue_txt_pb2._TXLOCATIONINFO
_TXTMERGERREQARGS.fields_by_name['rdm_debug'].message_type = websearch2.proto.news_recommendation.rcm_queue.rcm_queue_txt_pb2._RDMDEBUGINFO
_TXTMERGERREQARGS.fields_by_name['req_source'].enum_type = websearch2.proto.news_recommendation.rcm_queue.rcm_queue_txt_pb2._EREQSOURCE
_TXTMERGERRESPONSE.fields_by_name['user'].message_type = websearch2.proto.news_recommendation.rcm_queue.rcm_queue_req_pb2._USERINFO
_TXTMERGERRESPONSE.fields_by_name['cf_seeds'].message_type = _CFSEEDS
_TXTMERGERRESPONSE.fields_by_name['rsp_ext'].message_type = websearch2.proto.news_recommendation.rcm_queue.rcm_queue_txt_pb2._RSPEXT
_TXTMERGERSERVERRESPONSE.fields_by_name['rc'].enum_type = websearch2.proto.news_recommendation.rcm_queue.rcm_queue_rsp_pb2._RETURNCODE
_TXTMERGERSERVERRESPONSE.fields_by_name['strategy_info'].message_type = websearch2.proto.news_recommendation.guanxin_news_rcm_common_pb2._STRATEGYTRACK
_TXTMERGERSERVERRESPONSE.fields_by_name['rsp_ext_new'].message_type = websearch2.proto.news_recommendation.rcm_queue.rcm_queue_rsp_pb2._RSPEXTNEW

class TxtMergerRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TXTMERGERREQUEST
  
  # @@protoc_insertion_point(class_scope:pb.rcm.queue.txt.TxtMergerRequest)

class TxtMergerUserInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TXTMERGERUSERINFO
  
  # @@protoc_insertion_point(class_scope:pb.rcm.queue.txt.TxtMergerUserInfo)

class TxtMergerReqArgs(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TXTMERGERREQARGS
  
  # @@protoc_insertion_point(class_scope:pb.rcm.queue.txt.TxtMergerReqArgs)

class CFSeeds(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CFSEEDS
  
  # @@protoc_insertion_point(class_scope:pb.rcm.queue.txt.CFSeeds)

class TxtMergerResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TXTMERGERRESPONSE
  
  # @@protoc_insertion_point(class_scope:pb.rcm.queue.txt.TxtMergerResponse)

class TxtMergerServerResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TXTMERGERSERVERRESPONSE
  
  # @@protoc_insertion_point(class_scope:pb.rcm.queue.txt.TxtMergerServerResponse)

txt_merger_req.message_type = _TXTMERGERREQUEST
websearch2.proto.news_recommendation.rcm_queue.rcm_queue_pb2.Request.RegisterExtension(txt_merger_req)
txt_merger_user.message_type = _TXTMERGERUSERINFO
websearch2.proto.news_recommendation.rcm_queue.rcm_queue_req_pb2.UserInfo.RegisterExtension(txt_merger_user)
txt_merger_req_args.message_type = _TXTMERGERREQARGS
websearch2.proto.news_recommendation.rcm_queue.rcm_queue_req_pb2.ReqArgs.RegisterExtension(txt_merger_req_args)
txt_merger_rsp.message_type = _TXTMERGERRESPONSE
websearch2.proto.news_recommendation.rcm_queue.rcm_queue_pb2.Response.RegisterExtension(txt_merger_rsp)
# @@protoc_insertion_point(module_scope)