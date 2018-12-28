# -*- encoding:utf-8 -*-

__date__ = '2018/12/28/028 9:56'

from sqlalchemy import Column, Integer, String

from libs.base_model import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    openid = Column(String(50), unique=True)
    unionid = Column(String(50), unique=True)
    nickname = Column(String(20))
    headimgurl = Column(String(255))
    sex = Column(Integer, default=0)
    subscribe = Column(Integer)
    subscribe_time = Column(Integer)
    subscribe_scene = Column(String(100))
    area = Column(String(50))
    tagid_list = Column(String(100))
