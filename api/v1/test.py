# -*- encoding:utf-8 -*-

__date__ = '2018/12/25/025 18:30'

from libs.redprint import RedPrint

test_api = RedPrint("test")


@test_api.route("")
def test():
    return "test"
