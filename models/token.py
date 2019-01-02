# -*- encoding:utf-8 -*-

__date__ = '2019/1/2 17:54'

from sqlalchemy import Column, Integer, String

from libs.base_model import Base


class Token(Base):
    id = Column(Integer, primary_key=True)
    access_token = Column(String(255))
    token_type = Column(String(10))
    exp_timestamp = Column(Integer)
