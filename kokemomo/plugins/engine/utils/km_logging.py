#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler, HTTPHandler
from kokemomo.settings.common import LOGGER, PLUGINS

__author__ = 'hiroki'


class KMLogger:

    handlers = {}

    @classmethod
    def initHandlers(cls):
        if len(cls.handlers) == 0:
            mod = __import__('logging.handlers', fromlist=['RotatingFileHandler','HTTPHandler'])
            class_def = getattr(mod, "RotatingFileHandler")
            handler = class_def(
                filename=LOGGER['RotatingFileHandler']['filename'],
                maxBytes=LOGGER['RotatingFileHandler']['maxBytes'],
                backupCount=LOGGER['RotatingFileHandler']['backupCount'])
            formatter = logging.Formatter(LOGGER['RotatingFileHandler']['format'])
            handler.setFormatter(formatter)
            cls.handlers['RotatingFileHandler'] = handler

            class_def = getattr(mod, "HTTPHandler")
            handler = class_def(
                host=LOGGER['HTTPHandler']['host'],
                url=LOGGER['HTTPHandler']['url'],
                method=LOGGER['HTTPHandler']['method'])
            cls.handlers['HTTPHandler'] = handler

            sqllogger = logging.getLogger('sqlalchemy.pool')
            sqllogger.addHandler(cls.handlers['RotatingFileHandler'])
            sqllogger.setLevel(logging.CRITICAL)
            sqllogger = logging.getLogger('sqlalchemy.engine')
            sqllogger.addHandler(cls.handlers['RotatingFileHandler'])
            sqllogger.setLevel(logging.CRITICAL)
            sqllogger = logging.getLogger('sqlalchemy.orm.unitofwork')
            sqllogger.addHandler(cls.handlers['RotatingFileHandler'])
            sqllogger.setLevel(logging.CRITICAL)
            sqllogger = logging.getLogger('sqlalchemy.engine.base.Engine')
            sqllogger.addHandler(cls.handlers['RotatingFileHandler'])
            sqllogger.setLevel(logging.CRITICAL)

    @classmethod
    def get_handler(cls, name):
        return cls.handlers[name]

    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(self.__get_level(PLUGINS[name]['level']))
        handler = self.get_handler(PLUGINS[name]['logger'])
        self.logger.addHandler(handler)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def __get_level(self, level):
        if level == 'DEBUG':
            return logging.DEBUG
        elif level == 'INFO':
            return logging.INFO
        elif level == 'ERROR':
            return logging.ERROR
        elif level == 'WARNING':
            return logging.WARNING
        elif level == 'CRITICAL':
            return logging.CRITICAL

KMLogger.initHandlers()