# -*- encoding:utf-8 -*-

__date__ = '2018/12/27/027 18:49'

import hashlib
import requests
import time

from controller.token_controller import TokenController


access_token = ""
over_timestamp = 0


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


def get_token():
    token = TokenController.check_token("wechat")
    if token is False:
        payload_access_token = {
            'grant_type': 'client_credential',
            'appid': 'wx8ead9118850041df',
            'secret': '20a3c2d7e06e6bb956b89a66b7eef037'
        }
        token_url = 'https://api.weixin.qq.com/cgi-bin/token'
        timestamp = int(time.time())
        r = requests.get(token_url, params=payload_access_token)
        dict_result = (r.json())
        TokenController().create_token(dict_result['access_token'], "wechat", timestamp + dict_result['expires_in'])
        return dict_result["access_token"]
    return token.access_token


def get_media_id():
    img_url = 'https://api.weixin.qq.com/cgi-bin/media/upload'
    payload_img = {
        'access_token': get_token(),
        'type': 'image'
    }
    data = {'media': open("static/T002R300x300M000001CrpRT25yAN5.jpg", 'rb')}
    r = requests.post(url=img_url, params=payload_img, files=data)
    dict = r.json()
    return dict['media_id']
