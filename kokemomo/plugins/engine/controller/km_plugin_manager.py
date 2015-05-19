#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hiroki-m'

import logging
from urlparse import urljoin
from kokemomo.plugins.engine.utils.km_config import get_wsgi_setting
from kokemomo.plugins.engine.controller.km_data import KMData


logging.basicConfig(filename='kokemomo.log', level=logging.INFO, format='%(asctime)s %(message)s')

'''
Kokemomoプラグインマネージャ

プラグインに対する操作を行えます。

'''

name = get_wsgi_setting()
mod = __import__("kokemomo.plugins.engine.controller",fromlist=["km_wsgi"])
class_def = getattr(getattr(mod, "km_wsgi"), "WSGI_" + name)

plugins = {}


def get_root_plugin():
    return class_def.get_root_app()


def set_root_plugin(plugin):
    class_def.set_root_app(plugin)


def mount(rule, plugin):
    class_def.mount(rule, plugin)


def run():
    class_def.run()


def create_base_plugin(name):
    '''
    ベースプラグインを生成します。
    :return: ベースプラグインオブジェクト
    '''
    plugin = class_def()
    plugin.create_app()
    plugins[name] = plugin
    return plugin


def add_route(name, params):
    '''
    プラグインにルーティングの情報を追加します。
    必要な情報はプラグインベースオブジェクトの実装に依存します。
    ※詳細はkm_wsgiの使用する実装クラスのドキュメントを参照。

    :param plugin: ベースプラグインオブジェクト
    :param params: ルーティングの情報
    '''
    plugins[name].add_route(params)


def get_plugin(name):
    if name in plugins:
        return plugins[name]
    else:
        raise Exception('Target plugin not found.')


class KMBaseController(object):

    def __init__(self, name):
        self.name = name
        self.data = KMData(self)
        self.plugin = create_base_plugin(name)


    def get_url(self, routename, filename):
        return urljoin('/' + self.name + '/', self.plugin.app.get_url(routename, filename=filename))


    def add_route(self, rule, method, target, name=None):
        add_route(self.name, {'rule':rule, 'method':method, 'target':target, 'name':name})


    def render(self, template_path, **params):
        return self.plugin.render(template_path, params)


    def load_static_file(self, filename, root):
        return self.plugin.load_static_file(filename, root)