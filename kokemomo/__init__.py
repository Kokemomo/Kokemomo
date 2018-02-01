#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Contents Management System KOKEMOMO

"""

from beaker.middleware import SessionMiddleware
from kokemomo.plugins.engine.controller.km_backend.km_plugin_manager import KMPluginManager
from kokemomo.plugins.engine import engine
from kokemomo.plugins.admin import admin
from kokemomo.plugins import common_entry
from kokemomo.plugins import subapp
from kokemomo.plugins.blog import blog
from kokemomo.plugins.file_manager import file_manager
from kokemomo.plugins.engine.utils.km_logging import KMLogger
from kokemomo.settings import SETTINGS
from kokemomo.plugins.engine.model.km_storage import initialize
import application

initialize()

# session config
session_opts = {
    'session.type': 'ext:database',
    'session.url': 'sqlite:///session_data/session.db',
    'session.data_dir': './session_data',
    'session.cookie_expires': True,
    'session.auto': True
}

manager = KMPluginManager.get_instance()

manager.mount('/engine', engine)
manager.mount('/admin', admin)
manager.mount('/blog', blog)
manager.mount('/file_manager', file_manager)

plugin = SessionMiddleware(manager.get_root_plugin())
manager.set_root_plugin(plugin)

logger = KMLogger('kokemomo')
logger.info("KOKEMOMO ver." + SETTINGS.VERSION)

def app_run(port=None):
    if port is None:
        manager.run(SETTINGS.PORT)
    else:
        manager.run(port)
#        if app is not None:
#            runner(app, host='localhost', port=8861, debug=True, reloader=True)
    #        runner(app, host='localhost', port=8080, server='gunicorn', workers=1)
#        else:
#            raise SystemError
