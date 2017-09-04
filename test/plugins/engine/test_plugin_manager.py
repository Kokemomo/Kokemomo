#!/usr/bin/env python
# -*- coding:utf-8 -*-
from unittest import TestCase
from mox import Mox, ExpectedMethodCallsError
from nose.tools import ok_, eq_, raises, with_setup
from kokemomo.plugins.engine.controller.km_wsgi_rapper import WSGI_Bottle
from kokemomo.plugins.engine.controller.km_plugin_manager import create_base_plugin, add_route, plugins, get_plugin
from bottle import Bottle

__author__ = 'hiroki'

"""
km_plugin_managerのテスト.


"""

class PluginManagerTestCase(TestCase):

    @classmethod
    def setup_class(clazz):
        pass

    @classmethod
    def teardown_class(clazz):
        pass

    def setUp(self):
        self.mocker = Mox()
        plugins.clear()

    def tearDown(self):
        plugins.clear()

    def test_create_base_plugin(self):
        '''
        プラグイン生成のテスト

        ・プラグインが生成されることの確認

        :return:
        '''
        ok_(len(plugins) == 0) # 初期プラグイン数
        result = create_base_plugin('test') # testという名前のプラグインを生成
        ok_(isinstance(result, WSGI_Bottle)) # クラスを確認
        ok_(len(plugins) == 1) # プラグインが追加されたことを確認
        ok_(result is plugins['test']) # 取得できたプラグインと一覧に保持されたものが同一か確認

    def test_add_route(self):
        '''
        ルーティングのテスト

        ・pluginsの対象のプラグインのrouteが呼び出されることを確認

        :return:
        '''
        plugin = WSGI_Bottle() # テスト用にプラグインを生成
        plugins['test'] = plugin
        app_mock = self.mocker.CreateMock(Bottle)
        def test_method():
            pass
        app_mock.route(path='/test', method='GET', callback=test_method, name='test') # routeが呼び出された際の振る舞いを設定
        plugin.app = app_mock # プラグインのappを差し替え
        params = {'rule':'/test', 'method':'GET', 'target':test_method, 'name':'test'}
        self.mocker.ReplayAll()
        add_route('test', params)
        self.mocker.VerifyAll()


    def test_get_root_plugin(self):
        '''
        クラスメソッドの呼び出しだけなので不要
        :return:
        '''
        pass

    def test_set_root_plugin(self):
        '''
        クラスメソッドの呼び出しだけなので不要
        :return:
        '''
        pass


    def test_mount(self):
        '''
        クラスメソッドの呼び出しだけなので不要
        :return:
        '''
        pass


    def test_run(self):
        '''
        クラスメソッドの呼び出しだけなので不要
        :return:
        '''
        pass


    def test_get_plugin(self):
        '''
        プラグイン取得のテスト

        ・pluginsに追加したプラグインが、指定した名前で取得できることを確認

        :return:
        '''
        plugin =  create_base_plugin('test')
        plugins['test'] = plugin
        ok_(isinstance(plugin, get_plugin('test')))


    @raises(Exception)
    def test_get_plugin(self):
        '''
        プラグイン取得のテスト

        ・pluginsに存在しない名前を指定すると例外が発生する事を確認

        :return:
        '''
        plugin =  create_base_plugin('test')
        plugins['test'] = plugin
        ok_(isinstance(plugin, get_plugin('hoge')))


    # KMBaseControllerのテスト

