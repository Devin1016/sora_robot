# -*- encoding:utf-8 -*-

__date__ = '2018/12/25/025 18:27'

from flask import Blueprint

from api.v1.test import test_api


def blueprint_v1():
    bp_v1 = Blueprint("v1", __name__)

    test_api.register(bp_v1)

    return bp_v1
