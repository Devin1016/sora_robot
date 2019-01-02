# -*- encoding:utf-8 -*-

__date__ = '2018/12/27/027 19:13'

import xmltodict
import time

from flask import render_template

from .weather import get_weather
from .translate import get_trans
from .base import get_media_id
from controller.user_controller import UserController


class Message(object):
    def __init__(self, xml):
        msg = xmltodict.parse(xml).get("xml")
        self.to_user_name = msg.get("ToUserName", "")
        self.from_user_name = msg.get("FromUserName", "")
        self.create_time = msg.get("CreateTime", "")
        self.msg_type = msg.get("MsgType", "")
        self.event = msg.get("Event", "")
        self.event_key = msg.get("EventKey", "")
        self.ticket = msg.get("Ticket", "")
        self.latitude = msg.get("Latitude", "")
        self.longitude = msg.get("Longitude", "")
        self.precision = msg.get("Precison", "")
        self.event_key = msg.get("EventKey", "")
        self.msg_id = msg.get("MsgID", "")
        self.content = msg.get("Content", "")
        self.pic_url = msg.get("PicUrl", "")
        self.format = msg.get("Format", "")
        self.recognition = msg.get("Recognition", "")
        self.thumb_media_id = msg.get("ThumbMediaId", "")
        self.media_id = msg.get("MediaId", "")
        self.location_x = msg.get("Location_X", "")
        self.location_y = msg.get("Location_Y", "")
        self.scale = msg.get("Scale", "")
        self.label = msg.get("Label", "")
        self.title = msg.get("Title", "")
        self.description = msg.get("Description", "")
        self.url = msg.get("Url", "")
        self.music_url = ""

    def dispatch(self):
        if self.msg_type == "text":
            return self.text_msg_patch()
        elif self.msg_type == "image":
            pass
        elif self.msg_type == "voice":
            pass
        elif self.msg_type == "video":
            pass
        elif self.msg_type == "shortvideo":
            pass
        elif self.msg_type == "location":
            pass
        elif self.msg_type == "link":
            pass
        elif self.msg_type == "event":
            if self.event == "subscribe":
                UserController().create_user(self.from_user_name)
                self.msg_type = "music"
                self.title = "佛系少女-冯提莫"
                self.music_url = "https://api.mlwei.com/music/api/?key=523077333&type=url&id=004Mkw5K1oI9K9&size=m4a"
                self.thumb_media_id = get_media_id()
                res = Message.re_msg(self)
                return res
            pass

    def text_msg_patch(self):
        if "-w" in self.content:
            self.content = get_weather(self.content)
        elif "-t" in self.content:
            self.content = get_trans(self.content)
        elif "-m" in self.content:
            self.msg_type = "music"
            self.title = "佛系少女-冯提莫"
            self.music_url = "https://api.mlwei.com/music/api/?key=523077333&type=url&id=004Mkw5K1oI9K9&size=m4a"
            self.thumb_media_id = get_media_id()
        res = Message.re_msg(self)
        return res

    @staticmethod
    def re_msg(msg):
        msg.create_time = int(time.time())
        msg.to_user_name, msg.from_user_name = msg.from_user_name, msg.to_user_name
        if msg.msg_type == "text":
            return render_template("wechat_xml/text_message.xml", msg=msg)
        elif msg.msg_type == "image":
            return render_template("wechat_xml/img_message.xml", msg=msg)
        elif msg.msg_type == "voice":
            return render_template("wechat_xml/voice_message.xml", msg=msg)
        elif msg.msg_type == "video":
            return render_template("wechat_xml/video_message.xml", msg=msg)
        elif msg.msg_type == "music":
            return render_template("wechat_xml/music_message.xml", msg=msg)
        elif msg.msg_type == "news":
            return render_template("wechat_xml/ti_message.xml", msg=msg)
