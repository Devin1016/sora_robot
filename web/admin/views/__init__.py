# -*- encoding:utf-8 -*-

__date__ = '2018/12/25/025 18:42'

from flask import Blueprint

from web.admin.views.test import admin_rp


def blueprint_admin():
    bp_admin = Blueprint("admin", __name__)

    admin_rp.register(bp_admin)

    return bp_admin
