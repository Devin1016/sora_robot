# -*- encoding:utf-8 -*-

__date__ = '2018/12/27/027 10:04'

import time
import hashlib
import xml.etree.ElementTree as ET

from flask import Blueprint, request, make_response

wx = Blueprint("wx", __name__)


@wx.route("", method=["GET", "POST"])
def wx_interface():
    if request.method == "GET":
        token = "iccplay"
        data = request.args
        signature = data.get("signature", "")
        timestamp = data.get("timestamp", "")
        nonce = data.get("nonce", "")
        echostr = data.get("echostr", "")
        s = [timestamp, nonce, token]
        s.sort()
        s = "".join(s)
        if (hashlib.sha1(s).hexdigest() == signature):
            return make_response(echostr)
    else:
        rec = request.stream.read()
        xml_rec = ET.fromstring(rec)
        to_user_name = xml_rec.find("ToUserName").text
        from_user_name = xml_rec.find("FromUserName").text
        context = xml_rec.find("Content").text
        xml_rep = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"
        response = make_response(xml_rep % (
            from_user_name,
            to_user_name,
            str(int(time.time())),
            context
        ))
        response.content_type = "application/xml"
        return response
    return "Hello wx!"
