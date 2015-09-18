#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .km_plugin_manager import KMBaseController
from .km_exception import log

__author__ = 'hiroki'


class KMEngine(KMBaseController):

    def get_name(self):
        return 'engine'


    def get_route_list(self):
        list = (
            {'rule': '/engine-js/<filename>', 'method': 'GET', 'target': self.engine_js_static, 'name': 'engine_static_js'},
            {'rule': '/engine-css/<filename>', 'method': 'GET', 'target': self.engine_css_static, 'name': 'engine_static_css'},
            {'rule': '/engine-img/<filename>', 'method': 'GET', 'target': self.engine_img_static, 'name': 'engine_static_img'},
            {'rule': '/error', 'method': 'GET', 'target': self.engine_error},
        )
        return list


    @log
    def engine_js_static(self, filename):
        """
        set javascript files.
        :param filename: javascript file name.
        :return: static path.
        """
        file_path = 'kokemomo/plugins/engine/view/resource/js'
        return self.load_static_file(filename, root=file_path)

    @log
    def engine_css_static(self, filename):
        """
        set css files.
        :param filename: css file name.
        :return: static path.
        """
        file_path = 'kokemomo/plugins/engine/view/resource/css'
        return self.load_static_file(filename, root=file_path)

    @log
    def engine_img_static(self, filename):
        """
        set image files.
        :param filename: image file name.
        :return: static path.
        """
        file_path = 'kokemomo/plugins/engine/view/resource/img'
        return self.load_static_file(filename, root=file_path)

    def engine_error(self):
        return "An error has occurred." \
               " Please contact the server administrator."
