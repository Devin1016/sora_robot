# -*- encoding:utf-8 -*-

__date__ = '2018/12/25/025 18:46'

from libs.redprint import RedPrint

home_rp = RedPrint("home_rp")


@home_rp.route("")
def test():
    return "home_rp"
