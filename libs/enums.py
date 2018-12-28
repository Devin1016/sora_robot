# -*- encoding:utf-8 -*-

__date__ = '2018/12/28/028 10:37'

from enum import Enum


class WechatSubscribeScene(Enum):
    # 公众号搜索
    ADD_SCENE_SEARCH = 100
    # 公众号迁移
    ADD_SCENE_ACCOUNT_MIGRATION = 101
    # 名片分享
    ADD_SCENE_PROFILE_CARD = 102
    # 扫描二维码
    ADD_SCENE_QR_CODE = 103
    # 图文页内名称点击
    ADD_SCENEPROFILE = 104
    # 图文页右上角菜单
    ADD_SCENE_PROFILE_ITEM = 105
    # 支付后关注
    ADD_SCENE_PAID = 106
    # 其他
    ADD_SCENE_OTHERS = 107
