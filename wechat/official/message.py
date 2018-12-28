# -*- encoding:utf-8 -*-

__date__ = '2018/12/27/027 19:13'

import xmltodict
import time

from flask import render_template

from .weather import get_weather


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

    def dispatch(self):
        if self.msg_type == "text":
            return self.text_msg()
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
            pass

    def text_msg(self):
        self.content = get_weather(self.content)
        res = self.re_text_msg()
        return res

    def re_text_msg(self):
        self.to_user_name, self.from_user_name = self.from_user_name, self.to_user_name
        self.create_time = int(time.time())
        return render_template("wechat_xml/text_message.xml", msg=self)


