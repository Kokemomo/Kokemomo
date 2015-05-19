#!/usr/bin/env python
# -*- coding:utf-8 -*-

from mox import Mox, ExpectedMethodCallsError
from nose.tools import ok_, eq_, raises, with_setup
from kokemomo.plugins.engine.controller.km_wsgi import WSGI_Bottle
from kokemomo.plugins.engine.controller.km_plugin_manager import create_base_plugin, add_route, plugins
from kokemomo.lib.bottle import Bottle

__author__ = 'hiroki'

"""
km_plugin_managerのテスト.

前提条件：
    Kokemomoエンジンのプラグインのみ起動時に読み込まれるため、
    pluginsの初期サイズは1となる。s


"""

class TestPluginManager:

    @classmethod
    def setup_class(clazz):
        pass

    @classmethod
    def teardown_class(clazz):
        pass

    def setup(self):
        self.mocker = Mox()

    def teardown(self):
        pass

    def test_create_base_plugin(self):
        '''
        プラグイン生成のテスト
        :return:
        '''
        ok_(len(plugins) == 1) # 実行前はengineのみ
        result = create_base_plugin('test') # testという名前のプラグインを生成
        ok_(isinstance(result, WSGI_Bottle)) # クラスを確認
        ok_(len(plugins) == 2) # プラグインが追加されたことを確認
        ok_(result is not plugins['engine']) # engineのプラグインとは異なることを確認
        ok_(result is plugins['test']) # 取得できたプラグインと一覧に保持されたものが同一か確認

    def test_add_route(self):
        '''
        ルーティングのテスト
        nameが指定された場合
        :return:
        '''
        plugin = WSGI_Bottle() # テスト用にプラグインを生成
        app_mock = self.mocker.CreateMock(Bottle)
        def test_method():
            pass
        app_mock.route(path='/test', method='GET', callback=test_method, name='test') # routeが呼び出された際の振る舞いを設定
        plugin.app = app_mock # プラグインのappを差し替え
        params = {'rule':'/test', 'method':'GET', 'target':test_method, 'name':'test'}
        self.mocker.ReplayAll()
        add_route(plugin, params)
        self.mocker.VerifyAll()

    def test_add_route_noname(self):
        '''
        ルーティングのテスト
        nameが指定されない場合
        :return:
        '''
        plugin = WSGI_Bottle()
        app_mock = self.mocker.CreateMock(Bottle)
        def test_method():
            pass
        app_mock.route(path='/test', method='GET', callback=test_method, name=None)
        plugin.app = app_mock
        params = {'rule':'/test', 'method':'GET', 'target':test_method}
        self.mocker.ReplayAll()
        add_route(plugin, params)
        self.mocker.VerifyAll()