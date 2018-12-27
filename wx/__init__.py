# -*- encoding:utf-8 -*-

__date__ = '2018/12/27/027 10:04'

from flask import Blueprint


def blueprint_wx():
    bp_wx = Blueprint("wx", __name__)

    return bp_wx
