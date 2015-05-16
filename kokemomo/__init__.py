#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Contents Management System KOKEMOMO

"""

from kokemomo.lib.bottle import route, run as runner, request, response, redirect, template, get, url
from kokemomo.lib.bottle import static_file, default_app
from kokemomo.plugins.engine import plugin as engine
from kokemomo.plugins import common_entry
from kokemomo.plugins import subapp
from kokemomo.plugins import blog
import application
from beaker.middleware import SessionMiddleware


# session config
session_opts = {
    'session.type': 'ext:database',
    'session.url': 'sqlite:///session_data/session.db',
    'session.data_dir': './session_data',
    'session.cookie_expires': True,
    'session.auto': True
}

# sub subapp mount
app = default_app()
#from kokemomo.plugins import fb_login
app.mount('/engine', engine.app)
app.mount('/subapp', subapp)
#app.mount('/fb_login', fb_login)
app.mount('/application', application)
app.mount('/common_entry', common_entry)
app.mount('/blog', blog)
app = SessionMiddleware(app, session_opts)

VERSION = "0.6.8.1"
print("KOKEMOMO ver." + VERSION)


@route('/')
def top():
    """
    redirect to /engine url.
    """
    redirect('/engine/login')

def app_run():
        if app is not None:
            runner(app, host='localhost', port=8861, debug=True, reloader=True)
    #        runner(app, host='localhost', port=8080, server='gunicorn', workers=1)
        else:
            raise SystemError
