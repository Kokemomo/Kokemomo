#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler, HTTPHandler
from .km_config import (
    get_logging_setting,
    get_logging_setting_by_name,
    get_plugin_setting,
    get_plugin_setting_by_name,
)

__author__ = 'hiroki'

handlers = {}

def initHandlers():
    handler_names = get_logging_setting()
    for hadler_name in handler_names['handler']:
        settings = get_logging_setting_by_name(hadler_name)
        if hadler_name == "RotatingFileHandler":
            handler = createRotatingFileHandler(settings)
        elif hadler_name == "HTTPHandler":
            handler = createHTTPHandler(settings)

        if 'format' in settings:
            formatter = logging.Formatter(settings['format'])
            handler.setFormatter(formatter)
        handlers[hadler_name] = handler


def createRotatingFileHandler(settings):
    mod = __import__("logging.handlers", fromlist=["RotatingFileHandler"])
    class_def = getattr(mod, "RotatingFileHandler")
    handler = class_def(
        filename=settings['filename'],
        maxBytes=settings['maxBytes'],
        backupCount=settings['backupCount'])
    return handler


def createHTTPHandler(settings):
    mod = __import__("logging.handlers", fromlist=["HTTPHandler"])
    class_def = getattr(mod, "HTTPHandler")
    handler = class_def(
        host=settings['host'],
        url=settings['url'],
        method=settings['method'])
    return handler

initHandlers()
sqllogger = logging.getLogger('sqlalchemy.engine')
sqllogger.addHandler(handlers['RotatingFileHandler'])
sqllogger.setLevel(logging.INFO)
sqllogger = logging.getLogger('sqlalchemy.orm.unitofwork')
sqllogger.addHandler(handlers['RotatingFileHandler'])
sqllogger.setLevel(logging.INFO)

class KMLogger:
    def __init__(self, name):
        settings = get_plugin_setting_by_name(name)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(self.__get_level(settings))
        handler = handlers[settings['logger']]
        self.logger.addHandler(handler)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def __get_level(self, settings):
        level = settings['level']
        if level == 'DEBUG':
            return logging.DEBUG
        elif level == 'INFO':
            return logging.INFO
        elif level == 'ERROR':
            return logging.ERROR