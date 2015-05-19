#!/usr/bin/env python
# -*- coding: utf-8 -*-



import json

from kokemomo.plugins.engine.controller.km_plugin_manager import KMBaseController
from kokemomo.plugins.engine.controller.km_exception import log
from kokemomo.plugins.engine.controller.km_access_check import check_login
from kokemomo.plugins.engine.controller.km_login import logout, login_auth
from kokemomo.plugins.engine.utils.km_utils import get_menu_list

__author__ = 'hiroki'

class KMEngine(KMBaseController):


    def __init__(self):
        super(KMEngine, self).__init__('engine')
        self.add_route('/js/<filename>','GET', self.js_static, 'static_js')
        self.add_route('/css/<filename>','GET', self.css_static, 'static_css')
        self.add_route('/img/<filename>','GET', self.img_static, 'static_img')
        self.add_route('/error', 'GET', self.engine_error)


    @log
    def js_static(self, filename):
        """
        set javascript files.
        :param filename: javascript file name.
        :return: static path.
        """
        return self.load_static_file(filename, root='kokemomo/plugins/engine/view/resource/js')


    @log
    def css_static(self, filename):
        """
        set css files.
        :param filename: css file name.
        :return: static path.
        """
        return self.load_static_file(filename, root='kokemomo/plugins/engine/view/resource/css')


    @log
    def img_static(self, filename):
        """
        set image files.
        :param filename: image file name.
        :return: static path.
        """
        return self.load_static_file(filename, root='kokemomo/plugins/engine/view/resource/img')


    def engine_error(self):
        return "An error has occurred. Please contact the server administrator."
