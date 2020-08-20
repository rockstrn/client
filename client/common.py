#!/usr/bin/python
#-*- encoding:UTF-8 -*-
from websearch2.proto.news_recommendation.guanxin_news_rcm_pb2 import *
import random
import struct
import hashlib
import sys


def FillCkvData(base_user_info, user_model, user_action, user_action_weekend, video_dedup, user_action_and_model):
    #Õ¹Ê¾¼ÇÂ¼

    info_action = user_action_and_model["user_action"]

    for key in info_action.keys():
        exec("base_user_info.%s = user_action[info_action[key]]"%key)

    if user_action.has_key("ECKI_SHOW_LOG_WEISHI"):
        base_user_info.weishi_showlog_info = user_action["ECKI_SHOW_LOG_WEISHI"]
    base_user_info.video_show_docs = video_dedup
    if user_action_weekend.has_key("ECKI_SHOW_LOG_WEEKEND"):
        base_user_info.showlog_weekend = user_action_weekend["ECKI_SHOW_LOG_WEEKEND"]
    if user_action.has_key("ECKI_CLICK_LOG_WEEKEND"):
        base_user_info.clicklog_weekend = user_action_weekend["ECKI_CLICK_LOG_WEEKEND"]

    #ÓÃ»§Ä£ÐÍÊý¾Ý
    #base_user_info.tag_beta_info = user_model["ECKI_TAG_MODEL_BETA"]


    info_model = user_action_and_model["user_model"]
    for key in info_model.keys():
        exec("base_user_info.%s = user_model[info_model[key]]" % key)

def createSeqno():
    seq_no = "seqno_for_test_from_client_%d" % random.randint(0, 2000000000)
    return struct.unpack("QQ", hashlib.md5(seq_no).digest())[0]
