# -*- encoding:utf-8 -*-

__date__ = '2018/12/25/025 17:59'

from datetime import datetime

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from libs.error_code import ServerError


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, "keys") and hasattr(o, "__getitem__"):
            return dict(o)
        if isinstance(o, datetime):
            return o.strftime("%Y-%m-%d")
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder

    def __init__(self, import_name):
        super(Flask, self).__init__(import_name)
        self.config.from_pyfile("config/setting.py")
