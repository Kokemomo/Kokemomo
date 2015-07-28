#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Contents Management System KOKEMOMO

"""

from kokemomo.plugins.engine import engine
from kokemomo.plugins.admin import admin
from kokemomo.plugins import common_entry
from kokemomo.plugins import subapp
from kokemomo.plugins import blog
import application
from beaker.middleware import SessionMiddleware
from kokemomo.plugins.engine.controller.km_plugin_manager import mount, run, get_root_plugin, set_root_plugin
from kokemomo.plugins.engine.controller.km_storage import db

db.init()

# session config
session_opts = {
    'session.type': 'ext:database',
    'session.url': 'sqlite:///session_data/session.db',
    'session.data_dir': './session_data',
    'session.cookie_expires': True,
    'session.auto': True
}

mount('/engine', engine)
mount('/admin', admin)

plugin = SessionMiddleware(get_root_plugin())
set_root_plugin(plugin)

# sub subapp mount
#app = default_app()
#from kokemomo.plugins import fb_login
#app.mount('/engine', engine.app)
#app.mount('/subapp', subapp)
#app.mount('/fb_login', fb_login)
#app.mount('/application', application)
#app.mount('/common_entry', common_entry)
#app.mount('/blog', blog)
#app = SessionMiddleware(app, session_opts)

VERSION = "0.6.8.1"
print("KOKEMOMO ver." + VERSION)


def app_run():
    run()
#        if app is not None:
#            runner(app, host='localhost', port=8861, debug=True, reloader=True)
    #        runner(app, host='localhost', port=8080, server='gunicorn', workers=1)
#        else:
#            raise SystemError
