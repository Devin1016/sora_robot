# -*- encoding:utf-8 -*-

__date__ = '2018/12/27/027 18:49'

import hashlib


def wechat_validate(data):
    token = "iccplay"
    signature = data.get("signature", "")
    timestamp = data.get("timestamp", "")
    nonce = data.get("nonce", "")
    echostr = data.get("echostr", "")
    s = [timestamp, nonce, token]
    s.sort()
    s = "".join(s)
    if hashlib.sha1(s.encode("utf-8")).hexdigest() == signature:
        return echostr
    else:
        return False
