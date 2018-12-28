# -*- encoding:utf-8 -*-

__date__ = '2018/12/28/028 14:11'

from flask import request

from libs.redprint import RedPrint
from .base import wechat_validate
from .message import Message

official = RedPrint("official")


@official.route("", methods=["GET", "POST"])
def wechat_interface():
    if request.method == "GET":
        data = request.args
        res = wechat_validate(data)
        if res is not False:
            return res
    else:
        xml_rec = request.stream.read()
        msg = Message(xml_rec)
        msg.massage_path()
    return "Hello wechat!"
