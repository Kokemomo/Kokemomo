#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from kokemomo.plugins.engine.controller.km_engine import KMEngine
from kokemomo.plugins.engine.controller.km_exception import log as log_error

from kokemomo.settings import SETTINGS
from kokemomo.plugins.engine.utils.km_utils import create_result

class KMFileManager(KMEngine):

    def get_name(self):
        return 'file_manager'

    def get_route_list(self):
        list = super(KMFileManager, self).get_route_list() # import engine route list
        list = list + (
            {'rule': '/view/<filepath:path>', 'method': 'GET', 'target': self.file_view, 'name': 'file_view'},
        )
        return list

    @log_error
    def file_view(self, filepath):
        print(filepath)
        return self.load_static_file(filepath, root='kokemomo/data')