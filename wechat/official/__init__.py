# -*- encoding:utf-8 -*-

__date__ = '2018/12/28/028 14:11'

from flask import request, render_template

from libs.redprint import RedPrint
from .base import wechat_validate
from .message import Message

official = RedPrint("official")


@official.route("", methods=["GET", "POST"])
def wechat_interface():
    data = request.args
    res = wechat_validate(data)
    if request.method == "GET":
        if res is not False:
            return res
    else:
        if res is not False:
            xml_rec = request.stream.read()
            msg = Message(xml_rec)
            res = msg.dispatch()
            return res
    return "Hello wechat!"
