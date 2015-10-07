#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .km_session_manager import get_value_to_session
from kokemomo.settings import SETTINGS

__author__ = 'hiroki-m'


class KMData(object):

    def __init__(self, controller):
        self.controller = controller

    def get_request(self):
        return self.controller.plugin.get_request()

    def get_response(self):
        return self.controller.plugin.get_response()

    def get_request_parameter(self, name, default=None, decode=False):
        param = self.controller.plugin.get_request_parameter(name, default)
        if param == 'None':
            param = default
            return param
        if decode:
            return param.decode(SETTINGS.CHARACTER_SET)
        else:
            return param

    def get_user_id(self):
        request = self.controller.plugin.get_request()
        return get_value_to_session(request, 'user_id')
