#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urlparse import urljoin
from kokemomo.plugins.engine.controller.km_plugin_manager import plugins

__author__ = 'hiroki-m'

class KMBaseController:
    @classmethod
    def get_plugin(cls, name):
        if name in plugins:
            return plugins[name]
        else:
            raise Exception('target plugin not found.')

    @classmethod
    def get_url(cls, name, routename, filename):
        return urljoin('/' + name + '/', cls.get_plugin(name).app.get_url(routename, filename=filename))
