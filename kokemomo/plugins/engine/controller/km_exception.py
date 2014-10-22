#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'hiroki'

import logging
import traceback

"""
Exception class for Kokemomo CMS.

Outputs to the log by distinguishing the exception of the Application and KOKEMOMO.
Can be output by adding a "@log" to the method.

example:
from kokemomo.plugins.engine.controller.km_exception import log, KMException

@log
def function():
    raise KMException('message')

"""

class KMException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)

def log(callback):
    def wrapper(*args, **kwargs):
        try:
            return callback(*args, **kwargs)
        except KMException as kme:
            logging.error("An error has occurred in the kokemomo.")
            logging.error(traceback.format_exc())
            logging.error(kme.msg)
            raise kme
        except Exception as e:
            logging.error("An error has occurred in the application.")
            logging.error(traceback.format_exc())
            raise e
    return wrapper