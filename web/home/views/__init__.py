# -*- encoding:utf-8 -*-

__date__ = '2018/12/25/025 18:42'

from flask import Blueprint

from web.home.views.test import home_rp


def blueprint_home():
    bp_home = Blueprint("home", __name__)

    home_rp.register(bp_home)

    return bp_home
