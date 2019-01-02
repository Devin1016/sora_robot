# -*- encoding:utf-8 -*-

__date__ = '2019/1/2 12:01'

import requests
import random
import hashlib


def get_trans(text):
    salt = str(random.randint(1000000, 9999999))
    sign = make_sign(text[2:], salt)
    result = requests.get(
        url="http://api.fanyi.baidu.com/api/trans/vip/translate",
        params={
            "q": text[2:],
            "from": "auto",
            "to": "zh",
            "appid": "20190102000253952",
            "salt": salt,
            "sign": sign
        }
    ).json()
    return trans_parse(result)


def make_sign(q, salt):
    s = "20190102000253952" + q + salt + "AcDetml3yB7ZdEm2i_Se"
    sign = hashlib.md5(s.encode("utf-8")).hexdigest()
    return sign


def trans_parse(trans):
    result = trans.get("trans_result", "")[0]
    src = result.get("src", "")
    dst = result.get("dst", "")
    return "原文：{}\n 翻译：{}".format(src, dst)
