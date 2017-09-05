#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from abc import ABCMeta, abstractmethod
from urllib.parse import urljoin
from functools import wraps
from kokemomo.settings import SETTINGS
from ...utils.km_logging import KMLogger
from ..km_data import KMData

__author__ = 'hiroki-m'


'''
Kokemomoプラグインマネージャ

プラグインに対する操作を行えます。

'''

class KMPluginManager():

    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()

        return cls._instance

    def __init__(self):
        mod = __import__("kokemomo.plugins.engine.controller.km_backend", fromlist=["km_fw_wrapper"])
        self.class_def = getattr(getattr(mod, "km_fw_wrapper"), SETTINGS.BACKEND_NAME)
        self.plugins = {}


    def get_root_plugin(self):
        return self.instance.get_root_app()

    def set_root_plugin(self, plugin):
        self.instance.set_root_app(plugin)

    def mount(self, rule, plugin):
        self.instance.mount(rule, plugin)

    def run(self, port):
        self.instance.run(port)


    def create_base_plugin(self, name):
        '''
        ベースプラグインを生成します。
        :return: ベースプラグインオブジェクト
        '''
        self.instance = self.class_def()
        self.instance.create_app()
        self.plugins[name] = self.instance
        return self.instance


    def add_route(self, name, params):
        '''
        プラグインにルーティングの情報を追加します。
        必要な情報はプラグインベースオブジェクトの実装に依存します。
        ※詳細はkm_wsgiの使用する実装クラスのドキュメントを参照。

        :param plugin: ベースプラグインオブジェクト
        :param params: ルーティングの情報
        '''
        self.plugins[name].add_route(params)


    def get_plugin(self, name):
        if name in self.plugins:
            return self.plugins[name]
        else:
            raise Exception('Target plugin not found.')


class KMBaseController(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.name = self.get_name()
        self.logger = KMLogger(self.get_name())
        self.data = KMData(self)
        self.result = {}
        self.plugin = KMPluginManager.get_instance().create_base_plugin(self.name)
        for route in self.get_route_list():
            if 'name' in route:
                self.add_route(route['rule'], route['method'], route['target'], route['name'])
            else:
                self.add_route(route['rule'], route['method'], route['target'])

    @staticmethod
    def action(template=None):
        '''

        :param template:
        :return:
        '''
        def _action(callback):
            @wraps(callback)
            def wrapper(*args, **kwargs):
                res = callback(*args, **kwargs)
                if template is None:
                    return res
                else:
                    # args[0]はself
                    args[0].result['url'] = args[0].get_url
                    args[0].result['user_id'] = args[0].data.get_user_id()
                    return args[0].render(template, result=args[0].result)
            return wrapper
        return _action

    def check_login():
        """
        """
        def _check_login(callback):
            @wraps(callback)
            def wrapper(*args, **kwargs):
                user_id = args[0].data.get_user_id()
                if user_id is not None:
                    return callback(*args, **kwargs)
                return args[0].redirect('/engine/error')
            return wrapper
        return _check_login


    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_route_list(self):
        pass

    def get_url(self, routename, filename):
        return urljoin('/' + self.name + '/',
                       self.plugin.app.get_url(routename, filename=filename))

    def add_route(self, rule, method, target, name=None):
        self.plugin.add_route(
            {'rule': rule, 'method': method, 'target': target, 'name': name}
        )

    def render(self, template_path, **params):
        return self.plugin.render(template_path, params)

    def load_static_file(self, filename, root):
        # TODO 他のプラグインからの読み込みに対応する必要がある
        return self.plugin.load_static_file(filename, root)

    def redirect(self, url, code=None):
        self.plugin.redirect(url, code)