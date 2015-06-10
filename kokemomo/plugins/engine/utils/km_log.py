#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler
from .km_config import get_logging_setting

__author__ = 'hiroki'

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
logging.getLogger('sqlalchemy.orm.unitofwork').setLevel(logging.INFO)

class KMLogger:
    def __init__(self, name):
        settings = get_logging_setting()

        self.logger = logging.getLogger(name)
        self.logger.setLevel(self.__get_level(settings))

        formatter = logging.Formatter(settings['format'])

        # TODO ここはファクトリメソッド化する
        mod = __import__(
            "logging.handlers", fromlist=["RotatingFileHandler"])
        class_def = getattr(mod, "RotatingFileHandler")
        handler = class_def(
            settings['filename'],
            maxBytes=settings['maxbytes'],
            backupCount=settings['backupcount'])
        handler.setFormatter(formatter)
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