# -*- encoding:utf-8 -*-

__date__ = '2018/12/25/025 18:45'

from libs.redprint import RedPrint

admin_rp = RedPrint("admin_rp")


@admin_rp.route("")
def test():
    return "admin_rp"
