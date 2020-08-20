#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2017 tencent.com, Inc. All Rights Reserved
#
################################################################################
import struct
import hashlib
import cmem
import l5sys
import time
import datetime
import binascii
from configobj import ConfigObj
from ConfigParser import ConfigParser

class CkvAccess():
    def __init__(self):
        self.keys = list()
        self.error_message = ""
        self.cmem_api = cmem.CmemAPI()

    def error_message(self):
        return self.error_messge

    def init(self, modid, cmdid, bid):
        self.modid = modid
        self.cmdid = cmdid
        self.bid = bid
        self.keys = list()

    def addKey(self, key):
        self.keys.append(key)

    def query(self):
        l5_param = {}
        l5_param["modId"] = self.modid
        l5_param["cmdId"] = self.cmdid
        ret, qos = l5sys.ApiGetRoute(l5_param, 0.2)
        if ret != 0:
            self.error_message = "get ckv l5 %d:%d error %d" % (self.modid, self.cmdid, ret)
            return None

        addr = [(qos['hostIp'], qos['hostPort'])]
        self.cmem_api.config_server_addr(addr, 200)

        keys = list()
        for key in self.keys:
            keys.append((key, 0, -1))
        return self.cmem_api.getlist(self.bid, keys)

class KdCkvAccess(object):
    def __init__(self, printlog = False):
        #ÓÃ»§»­Ïñkey

        #ÓÃ»§ÐÐÎªkey

        self.myprintlog = printlog
        self.ckvaccess = CkvAccess()

    def myprint(self, message):
        if (self.myprintlog == True):
            print message

    def genKey(self, uin, idx, week = 0):
    	md5 = struct.unpack("QQ", hashlib.md5(uin).digest())[0]
        week = week << 5
        idx = week | idx
        return struct.pack("QB", md5, idx)

    def genNewKey(self, uin, idx, weekday):
    	md5 = struct.unpack("QQ", hashlib.md5(uin).digest())[0]
        return struct.pack("QHH", md5, idx, weekday)


    def getUserModel(self, modid, cmdid, bid, uin, model_key_txt):
        self.ckvaccess.init(modid, cmdid, bid)

        # int => str
        for key in model_key_txt.keys():
            #print modid
            self.ckvaccess.addKey(self.genKey(uin, key))
        result = self.ckvaccess.query()

        if result is None:
            print "get %s user model error" % uin
            return None

        self.myprint("\n%s User Module" % uin)
        usermodel = dict()
        for item in (result):
            key_int = struct.unpack("QB", item[0])[1]
            usermodel[model_key_txt[key_int]] = ""
            if item[2] == -13106 or item[2] == -13200:
                self.myprint("%s:%d notexist" % (model_key_txt[key_int], key_int))
                continue
            if item[2] != 0:
                self.myprint("%s:%d errorcode %d" % (model_key_txt[key_int], key_int, item[2]))
                continue
            if len(item[1]) <= 0:
                self.myprint("%s:%d nodata" % (model_key_txt[key_int], key_int))
                continue

            self.myprint("%s:%d len:%d" % (model_key_txt[key_int], key_int, len(item[1])))
            #self.myprint("%s:%d len:%d" % (self.user_model_key_txt[key_int], key_int, item[1]))
            usermodel[model_key_txt[key_int]] = item[1]

        return usermodel

    def getUserActionWeekend(self, modid, cmdid, bid, uin, action_key_txt):
        self.ckvaccess.init(modid, cmdid, bid)
        week = datetime.datetime.now().weekday()
        showlog_weekend_keys = dict();
        clicklog_weekend_keys = dict();
        for key, value in action_key_txt.items():
            if (value == "ECKI_SHOW_LOG_WEEKEND"):
                raw_time = (int)(time.time())
                days = (raw_time + 8 * 60 * 60) / (24 * 60 * 60) - week - 2
                self.ckvaccess.addKey(self.genNewKey(uin, key, days))
                showlog_weekend_keys[self.genNewKey(uin, key, days)] = 1;
                self.ckvaccess.addKey(self.genNewKey(uin, key, days + 1))
                showlog_weekend_keys[self.genNewKey(uin, key, days + 1)] = 1;
                continue


        result = self.ckvaccess.query()

        if result is None:
            print "get %d user action error" % uin
            return None

        self.myprint("\n%s User Action weekend" % uin)
        useraction = dict()
        for item in (result):
            if (item[0] in showlog_weekend_keys):
                if (useraction.has_key("ECKI_SHOW_LOG_WEEKEND")):
                    useraction["ECKI_SHOW_LOG_WEEKEND"] += item[1]
                else:
                    useraction["ECKI_SHOW_LOG_WEEKEND"] = item[1]
                day = struct.unpack("QHH", item[0])[2]
                key_int = struct.unpack("QHH", item[0])[1]

                self.myprint("%s:%d:%d len:%d" % ("ECKI_SHOW_LOG_WEEKEND", key_int, day, len(item[1])))
                continue


            key_int = struct.unpack("QB", item[0])[1] & 0x1F
            useraction[action_key_txt[key_int]] = ""
        for item in (result):
            if (item[0] in showlog_weekend_keys):
                if (useraction.has_key("ECKI_SHOW_LOG_WEEKEND")):
                    useraction["ECKI_SHOW_LOG_WEEKEND"] += item[1]
                else:
                    useraction["ECKI_SHOW_LOG_WEEKEND"] = item[1]
                day = struct.unpack("QHH", item[0])[2]
                key_int = struct.unpack("QHH", item[0])[1]
                self.myprint("%s:%d:%d len:%d" % ("ECKI_SHOW_LOG_WEEKEND", key_int, day, len(item[1])))
                continue

            if (item[0] in clicklog_weekend_keys):
                if (useraction.has_key("ECKI_CLICK_LOG_WEEKEND")):
                    useraction["ECKI_CLICK_LOG_WEEKEND"] += item[1]
                else:
                    useraction["ECKI_CLICK_LOG_WEEKEND"] = item[1]
                day = struct.unpack("QHH", item[0])[2]
                key_int = struct.unpack("QHH", item[0])[1]
                self.myprint("%s:%d:%d len:%d" % ("ECKI_CLICK_LOG_WEEKEND", key_int, day, len(item[1])))
                continue

        return useraction

    def getUserAction(self, modid, cmdid, bid, uin, action_key_txt):
        self.ckvaccess.init(modid, cmdid, bid)
        week = datetime.datetime.now().weekday()
        showlog_weekend_keys = dict();
        for key, value in action_key_txt.items():
            if (value == "ECKI_CLICK_LOG" or value == "ECKI_VIDEO_CLICK_LOG" or value == "ECKI_SHORT_VIDEO_CLICK_LOG" or value == "ECKI_TINY_VIDEO_CLICK_LOG"):
                #self.myprint("%s:%s" % (key, binascii.hexlify(self.genKey(uin, self.user_action_key[key]))))
                self.ckvaccess.addKey(self.genKey(uin, key))
                continue

            for i in (0, 1, 2, 3):
                getweek = ((week + 7 - i) % 7) + 1
                #self.myprint("%s:%d:%s" % (key, getweek, binascii.hexlify(self.genKey(uin, self.user_action_key[key], getweek))))
                self.ckvaccess.addKey(self.genKey(uin, key, getweek))

        result = self.ckvaccess.query()

        if result is None:
            print "get %d user action error" % uin
            return None

        self.myprint("\n%s User Action" % uin)
        useraction = dict()

        for item in (result):
            key_int = struct.unpack("QB", item[0])[1] & 0x1F
            #这里的key_int会出现不存在的数1个
            if not action_key_txt.has_key(key_int):
                continue
            # bug
            if not useraction.has_key(action_key_txt[key_int]):
                useraction[action_key_txt[key_int]] = ""
            week = struct.unpack("QB", item[0])[1] >> 5
            if item[2] == -13106 or item[2] == -13200:
                self.myprint("%s:%d:%d notexist" % (action_key_txt[key_int], key_int, week))
                continue
            if item[2] != 0:
                self.myprint("%s:%d:%d errorcode %d" % (action_key_txt[key_int], key_int, week, item[2]))
                continue
            if len(item[1]) <= 0:
                self.myprint("%s:%d:%d nodata" % (action_key_txt[key_int], key_int, week))
                continue

            self.myprint("%s:%d:%d len:%d" % (action_key_txt[key_int], key_int, week, len(item[1])))
            if useraction.has_key(action_key_txt[key_int]):
                useraction[action_key_txt[key_int]] += item[1]
            else:
                useraction[action_key_txt[key_int]] = item[1]

        return useraction

    def getTxtDedup(self,modid, cmdid, bid, uin, key_txt):
        ECKI_DOC_DEDUP_TXT = 22

        self.ckvaccess.init(modid, cmdid, bid)
        self.ckvaccess.addKey(self.genKey(uin, ECKI_DOC_DEDUP_TXT))
        result = self.ckvaccess.query()

        if result is None:
            print "get %s user model error" % uin
            return None

        self.myprint("\n%s Txt dedup" % uin)
        for item in (result):
            key_int = struct.unpack("QB", item[0])[1]
            if item[2] == -13106 or item[2] == -13200:
                self.myprint("%s:%d notexist" % ("ECKI_DOC_DEDUP_TXT", key_int))
                continue
            if item[2] != 0:
                self.myprint("%s:%d errorcode %d" % ("ECKI_DOC_DEDUP_TXT", key_int, item[2]))
                continue
            if len(item[1]) <= 0:
                self.myprint("%s:%d nodata" % ("ECKI_DOC_DEDUP_TXT", key_int))
                continue

            self.myprint("%s:%d len:%d" % ("ECKI_DOC_DEDUP_TXT", key_int, len(item[1])))
            return item[1]

        return None

    def getVideoDedup(self, modid, cmdid, bid, uin, video_key_txt):
        ECKI_DOC_DEDUP_VIDEO = 23

        self.ckvaccess.init(modid, cmdid, bid)
        self.ckvaccess.addKey(self.genKey(uin, ECKI_DOC_DEDUP_VIDEO))
        result = self.ckvaccess.query()

        if result is None:
            print "get %s user model error" % uin
            return None

        self.myprint("\n%s Txt dedup" % uin)
        for item in (result):
            key_int = struct.unpack("QB", item[0])[1]
            if item[2] == -13106 or item[2] == -13200:
                self.myprint("%s:%d notexist" % ("ECKI_DOC_DEDUP_VIDEO", key_int))
                continue
            if item[2] != 0:
                self.myprint("%s:%d errorcode %d" % ("ECKI_DOC_DEDUP_VIDEO", key_int, item[2]))
                continue
            if len(item[1]) <= 0:
                self.myprint("%s:%d nodata" % ("ECKI_DOC_DEDUP_VIDEO", key_int))
                continue

            self.myprint("%s:%d len:%d" % ("ECKI_DOC_DEDUP_VIDEO", key_int, len(item[1])))
            return item[1]

        return None


if __name__ == "__main__":
    kd_ckv_access = KdCkvAccess(True)
    user_moder = kd_ckv_access.getUserModel(64935489, 131072, 101480010, "3235177047")
    kd_ckv_access.getUserAction(64935489, 65536, 101480009, "3235177047")
    kd_ckv_access.getUserActionWeekend(64829505, 524288, 101500181, "3235177047")
    kd_ckv_access.getTxtDedup(64935489, 458752, 101011243, "3235177047")
    kd_ckv_access.getVideoDedup(64935489, 196608, 101011237, "3235177047")
