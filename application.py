# -*- encoding:utf-8 -*-

__date__ = '2018/12/25/025 18:04'

from werkzeug.exceptions import HTTPException

from libs import Flask
from libs.error_code import APIException, ServerError

app = Flask(__name__)

app.config.from_pyfile("config/setting.py")

from libs.base_model import db
from models.user import User
from models.token import Token

with app.app_context():
    db.create_all()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        if not app.config["DEBUG"]:
            return ServerError
        else:
            raise e
