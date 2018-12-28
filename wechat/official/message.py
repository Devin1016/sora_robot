# -*- encoding:utf-8 -*-

__date__ = '2018/12/27/027 19:13'

import xmltodict
import time

from flask import render_template

from libs.error_code import MessageTypeError


class Message:
    def __init__(self, xml):
        msg = xmltodict.parse(xml).get("xml")
        self.to_user_name = msg.get("ToUserName", "")
        self.from_user_name = msg.get("FromUserName", "")
        self.create_time = msg.get("CreateTime", "")
        self.msg_type = msg.get("MsgType", "")
        if self.msg_type == "event":
            self.event = msg.get("Event", "")
            if self.event == "subscribe" or self.event == "SCAN":
                self.event_key = msg.get("EventKey", "")
                self.ticket = msg.get("Ticket", "")
            elif self.event == "LOCATION":
                self.latitude = msg.get("Latitude", "")
                self.longitude = msg.get("Longitude", "")
                self.precision = msg.get("Precison", "")
            elif self.event == "CLICK" or self.event == "VIEW":
                self.event_key = msg.get("EventKey", "")
        else:
            self.msg_id = msg.get("MsgID", "")
            if self.msg_type == "text":
                self.content = msg.get("Content", "")
            elif self.msg_type == "image":
                self.pic_url = msg.get("PicUrl", "")
                self.media_id = msg.get("MediaId", "")
            elif self.msg_type == "voice":
                self.format = msg.get("Format", "")
                self.media_id = msg.get("MediaId", "")
                self.recognition = msg.get("Recognition", "")
            elif self.msg_type == "video" or self.msg_type == "shortvideo":
                self.thumb_media_id = msg.get("ThumbMediaId", "")
                self.media_id = msg.get("MediaId", "")
            elif self.msg_type == "location":
                self.location_x = msg.get("Location_X", "")
                self.location_y = msg.get("Location_Y", "")
                self.scale = msg.get("Scale", "")
                self.label = msg.get("Label", "")
            elif self.msg_type == "link":
                self.title = msg.get("Title", "")
                self.description = msg.get("Description", "")
                self.url = msg.get("Url", "")

    def massage_path(self):
        if self.msg_type == "text":
            pass
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
        return MessageTypeError

    def text_msg(self):
        self.to_user_name, self.from_user_name = self.from_user_name, self.to_user_name
        self.create_time = time.time()
        return render_template("wechat_xml/text_message.xml", msg=self), 200,  {'Content-Type': 'application/xml'}