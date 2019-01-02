# -*- encoding:utf-8 -*-

__date__ = '2019/1/2 17:59'

import time

from libs.base_model import db
from models.token import Token


class TokenController(Token):
    def create_token(self, token, token_type, exp_timestamp):
        with db.auto_commit():
            self.access_token = token
            self.token_type = token_type
            self.exp_timestamp = exp_timestamp
            db.session.add(self)

    @staticmethod
    def check_token(token_type):
        token = Token.query.filter_by(token_type=token_type).first()
        if token is not None and token.exp_timestamp > int(time.time()):
            return token
        else:
            return False
