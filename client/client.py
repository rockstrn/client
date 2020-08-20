import websearch2.proto.news_recommendation.newsrcm_score_pb2
import websearch2.proto.news_recommendation.newsrcm_txt_recall_pb2
import websearch2.proto.news_recommendation.guanxin_news_rcm_pb2
#from websearch2.proto.news_recommendation.guanxin_news_rcm_pb2 import NewsRcmRequest
#from websearch2.proto.news_recommendation.guanxin_news_rcm_pb2 import NewsRcmResult
#from websearch2.proto.news_recommendation.newsrcm_txt_recall_pb2 import Request
#from websearch2.proto.news_recommendation.newsrcm_txt_recall_pb2 import Response
#from websearch2.proto.news_recommendation.newsrcm_score_pb2 import Request
#from websearch2.proto.news_recommendation.newsrcm_score_pb2 import Result

from optparse import OptionParser
from configobj import ConfigObj
from ctypes import *
import string
import sys
import requests
import base64
import pbjson
import simplejson
import ckvhelper
import common

def ConfigOptionParser(parser):
    parser.add_option("", "--serverip", dest="serverip", help="server ip:port")
    parser.add_option("", "--url", dest="url", help="url", default="")
    parser.add_option("", "--reqfile", dest="reqfile", help="request file")
    parser.add_option("", "--servers", dest="servers", help="")
    parser.add_option("", "--isbase64", dest="isbase64", help="base64", default=0)

def get_model(kd_ckv_access, conf, uin, model_key_txt):
    model = conf["model"]
    return kd_ckv_access.getUserModel(int(model["modid"]), int(model["cmdid"]), int(model["bid"]), uin, model_key_txt)

def get_action(kd_ckv_access, conf, uin, action_key_txt):
    action = conf["action"]
    return kd_ckv_access.getUserAction(int(action["modid"]), int(action["cmdid"]), int(action["bid"]), uin, action_key_txt)

def get_video(kd_ckv_access, conf, uin, video_key_txt):
    video = conf["isvideo"]
    return kd_ckv_access.getVideoDedup(int(video["modid"]), int(video["cmdid"]), int(video["bid"]), uin, video_key_txt)

def get_txt(kd_ckv_access, conf, uin, txt_key_txt):
    txt = conf["istxt"]
    return kd_ckv_access.getTxtDedup(int(txt["modid"]), int(txt["cmdid"]), int(txt["bid"]), uin, txt_key_txt)

def get_action_weekend(kd_ckv_access, conf, uin, action_key_txt):
    weekend_action = conf["weekend_action"]
    return kd_ckv_access.getUserActionWeekend(int(weekend_action["modid"]), int(weekend_action["cmdid"]), int(weekend_action["bid"]), uin, action_key_txt)

def AccessServer(req, ret, url):
    const_header = {"Accept":"application/pb", "Content-Type":"application/pb"}
    print len(req.SerializeToString())
    print req
    rsp = requests.post(url, data=req.SerializeToString(), headers=const_header)
    ret.ParseFromString(rsp.content)
    return True

def ShowResponse(ret):
    print ret
    return True

def findreq(protocol, f):
    #libtxt_recall = CDLL("./libtxt_recall.so")
    #libtxt_recall.Init()
    if protocol == "stream":
        return pbjson.dict2pb(websearch2.proto.news_recommendation.guanxin_news_rcm_pb2.NewsRcmRequest, s)
       #return pbjson.dict2pb(so.NewsRcmRequest, s)
    elif protocol == "recall":
        return pbjson.dict2pb(websearch2.proto.news_recommendation.newsrcm_txt_recall_pb2.Request, s)
        #return pbjson.dict2pb(libtxt_recall._ZNK2pb3rcm5queue3txt17RelatedTxtRequest3hotEv, s)
    else:
        return pbjson.dict2pb(websearch2.proto.news_recommendation.newsrcm_score_pb2.Request, s)

def findres(protocol, f):
    #so = ctypes.cdll.LoadLibrary('./xrecall.so')
    #so = CDLL("./libtxt_recall.so")
    if protocol == "stream":
        return websearch2.proto.news_recommendation.guanxin_news_rcm_pb2.NewsRcmResult()
    elif protocol == "recall":
        return websearch2.proto.news_recommendation.newsrcm_txt_recall_pb2.Response()
    else:
        return websearch2.proto.news_recommendation.newsrcm_score_pb2.Result()

def FillCkvData(server_protocol, request, isvideo, conf):
    print "fill ckv info=========================="

    server = conf["servers"]
    action_tmp = conf['user_action_key']
    model_tmp = conf['user_model_key']

    action_key_txt = dict()
    for key in action_tmp.keys():
        #print int(key)
        action_key_txt[int(key)] = action_tmp[key]

    model_key_txt = dict()
    for key in model_tmp.keys():
        model_key_txt[int(key)] = model_tmp[key]

    video_key_txt = {23: "ECKI_DOC_DEDUP_VIDEO"}
    txt_key_txt = {22: "ECKI_DOC_DEDUP_TXT"}

    user_model_and_action = dict()
    user_model_and_action["user_model"] = conf["user_model"]
    user_model_and_action["user_action"] = conf["user_action"]


    kd_ckv_access = ckvhelper.getckv.KdCkvAccess(True)

    if server_protocol  == "stream" :
        struin = str(request.user_spec.uin)
    else:
        struin = str(request.user.qq)

    user_model = get_model(kd_ckv_access, conf, struin, model_key_txt)
    if user_model is None:
        print "get user model error"
        return None

    user_action = get_action(kd_ckv_access, conf, struin, action_key_txt)
    if user_action is None:
        print "get user action error"
        return None

    dedup = ""
    if isvideo == "video":
        dedup = get_video(kd_ckv_access, conf, struin, video_key_txt)
    else:
        dedup = get_txt(kd_ckv_access, conf, struin, txt_key_txt)
    if dedup is None:
        print "get video dedup error"
        return None

    user_action_weekend = get_action_weekend(kd_ckv_access, conf, struin, action_key_txt)
    if user_action_weekend is None:
        print "get action weekend error"
        return None
    print "==================================="

    if server_protocol == "recall":
        common.FillCkvData(request.user_model_and_action, user_model, user_action, user_action_weekend, dedup, user_model_and_action)
    else:
        common.FillCkvData(request.base_user_info, user_model, user_action, user_action_weekend, dedup, user_model_and_action)



if __name__ == "__main__":
    parser = OptionParser(usage="python client.py [options]")
    ConfigOptionParser(parser)
    (options, args) = parser.parse_args()

    conf_path = "conf.ini"
    conf = ConfigObj(conf_path, encoding='UTF-8')

    server = conf["servers"][options.servers]
    isvideo = server.split('/')[0]
    ckv = server.split('/')[1]
    server_protocol = server.split('/')[2]

    #protocol = conf[options.servers]["protocol"]

    if (options.serverip is None or options.reqfile is None):
        print "bad arguments"
        sys.exit(0)

    if not options.isbase64:
        f = file(options.reqfile)
        s = simplejson.load(f)
        f.close()
        request = findreq(server_protocol, f)
        result = findres(server_protocol, f)
    else:
        f = file(options.reqfile)
        s = f.read()
        request = base64.b64decode(s)
        f.close()
        result = findres(server_protocol, f)


    url = "http://%s/%s" % (options.serverip, options.url)

    if ckv == "ckv":
        FillCkvData(server_protocol, request, isvideo, conf)


    if not AccessServer(request, result, url):
        print "AccessServer() Error!"
        sys.exit(3)

    if not ShowResponse(result):
        print "ShowResponse() Error!"
        sys.exit(4)
    sys.exit(0)
