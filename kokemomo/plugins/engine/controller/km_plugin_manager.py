#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hiroki-m'

from kokemomo.plugins.engine.utils.km_config import get_wsgi_setting

'''
Kokemomoプラグインクラス
プラグインを作成する際には、__init__.pyにてこのクラスでベースプラグインを生成し、
ルーティングの登録を行う必要があります。

'''

name = get_wsgi_setting()
mod = __import__("kokemomo.plugins.engine.controller",fromlist=["km_wsgi"])
class_def = getattr(getattr(mod, "km_wsgi"), "WSGI_" + name)

plugins = {}


def create_base_plugin(name):
    '''
    ベースプラグインを生成します。
    :return: ベースプラグインオブジェクト
    '''
    plugin = class_def()
    plugin.create_app()
    plugins[name] = plugin
    return plugin


def add_route(plugin, params):
    '''
    プラグインにルーティングの情報を追加します。
    必要な情報はプラグインベースオブジェクトの実装に依存します。
    ※詳細はkm_wsgiの使用する実装クラスのドキュメントを参照。

    :param plugin: ベースプラグインオブジェクト
    :param params: ルーティングの情報
    '''
    plugin.add_route(params)

