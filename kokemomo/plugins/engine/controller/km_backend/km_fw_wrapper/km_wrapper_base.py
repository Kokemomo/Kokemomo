#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from kokemomo.settings import SETTINGS

class KMBaseFrameworkWrapper(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_root_app(self):
        pass


    @abstractmethod
    def set_root_app(self, app):
        pass


    @abstractmethod
    def mount(self, rule, plugin):
        pass


    @abstractmethod
    def run(self, port):
        pass


    @abstractmethod
    def create_app(self):
        pass


    @abstractmethod
    def add_route(self, params):
        pass


    @abstractmethod
    def get_request(self):
        pass


    @abstractmethod
    def get_response(self):
        pass


    @abstractmethod
    def get_request_parameter(self, name, default):
        pass


    @abstractmethod
    def render(self, template_path, params):
        pass


    @abstractmethod
    def load_static_file(self, filename, root):
        pass


    @abstractmethod
    def redirect(self, url, code):
        pass

