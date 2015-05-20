#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .km_plugin_manager import KMBaseController
from .km_exception import log

__author__ = 'hiroki'


class KMEngine(KMBaseController):

    def __init__(self):
        super(KMEngine, self).__init__('engine')
        self.add_route('/js/<filename>', 'GET', self.js_static, 'static_js')
        self.add_route('/css/<filename>', 'GET', self.css_static, 'static_css')
        self.add_route('/img/<filename>', 'GET', self.img_static, 'static_img')
        self.add_route('/error', 'GET', self.engine_error)

    @log
    def js_static(self, filename):
        """
        set javascript files.
        :param filename: javascript file name.
        :return: static path.
        """
        file_path = 'kokemomo/plugins/engine/view/resource/js'
        return self.load_static_file(filename, root=file_path)

    @log
    def css_static(self, filename):
        """
        set css files.
        :param filename: css file name.
        :return: static path.
        """
        file_path = 'kokemomo/plugins/engine/view/resource/css'
        return self.load_static_file(filename, root=file_path)

    @log
    def img_static(self, filename):
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
