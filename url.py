# -*- encoding:utf-8 -*-

__date__ = '2018/12/25/025 18:23'

from application import app

from web.admin.views import blueprint_admin
from web.home.views import blueprint_home
from wx import blueprint_wx
from api.v1 import blueprint_v1

app.register_blueprint(blueprint_admin(), url_prefix="/admin")
app.register_blueprint(blueprint_home(), url_prefix="/")
app.register_blueprint(blueprint_wx(), url_prefix="/wx")
app.register_blueprint(blueprint_v1(), url_prefix="/v1")
