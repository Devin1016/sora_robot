# -*- encoding:utf-8 -*-

__date__ = '2018/12/25/025 17:54'

from flask_script import Manager, Server

from application import app
import url


manager = Manager(app)

manager.add_command("runserver", Server(
    host="0.0.0.0",
    port=app.config["SERVER_PORT"]
))

if __name__ == "__main__":
    manager.run()
