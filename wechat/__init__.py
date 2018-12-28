# -*- encoding:utf-8 -*-

__date__ = '2018/12/27/027 10:04'

from flask import Blueprint

from wechat.official import official


def blueprint_wechat():
    bp_wechat = Blueprint("bp_wechat", __name__)

    official.register(bp_wechat)

    return bp_wechat
