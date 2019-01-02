# -*- encoding:utf-8 -*-

__date__ = '2019/1/2 16:24'

import time, requests

from models.user import User

from libs.base_model import db
from wechat.official.base import get_token


class UserController(User):
    def create_user(self, openid):
        if UserController.check_user(openid) is False:
            self.openid = openid
            user_info = UserController.get_wechat_info(openid)
            with db.auto_commit():
                self.openid = user_info.get("openid", "")
                self.unionid = user_info.get("unionid", "")
                self.nickname = user_info.get("nickname", "")
                self.headimgurl = user_info.get("headimgurl", "")
                self.sex = user_info.get("sex", "")
                self.subscribe = user_info.get("subscribe", "")
                self.subscribe_time = user_info.get("subscribe_time", "")
                self.subscribe_scene = user_info.get("subscribe_scene", "")
                self.area = user_info.get("country", "") + user_info.get("province", "") + user_info.get("city", "")
                self.tagid_list = "|".join(user_info.get("tagid_list", ""))
                db.session.add(self)

    @staticmethod
    def check_user(openid):
        user = User.query.filter_by(openid=openid).first()
        if user is None:
            return False
        return True

    @staticmethod
    def get_wechat_info(openid):
        payload_access_token = {
            'access_token': get_token(),
            'openid': openid,
            'lang': 'zh_CN'
        }
        token_url = 'https://api.weixin.qq.com/cgi-bin/user/info'
        r = requests.get(token_url, params=payload_access_token).json()
        return r
