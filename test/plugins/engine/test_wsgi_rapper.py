#!/usr/bin/env python
# -*- coding:utf-8 -*-
from unittest import TestCase
from mox import Mox, ExpectedMethodCallsError
from nose.tools import ok_, eq_, raises, with_setup
from kokemomo.plugins.engine.controller.km_wsgi_rapper import WSGI_Bottle
from kokemomo.plugins.engine.controller.km_plugin_manager import create_base_plugin, add_route, plugins
from kokemomo.lib.bottle import Bottle

__author__ = 'hiroki'

"""
km_wsgi_rapperのテスト.


"""

class WSGIRapperTestCase(TestCase):

    @classmethod
    def setup_class(clazz):
        pass

    @classmethod
    def teardown_class(clazz):
        pass

    def setUp(self):
        self.mocker = Mox()
        plugins.clear()

    def teardown(self):
        plugins.clear()


    def test_add_route(self):
        '''
        ルーティングのテスト
        nameが指定された場合
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

    def test_add_route_noname(self):
        '''
        ルーティングのテスト
        nameが指定されない場合
        :return:
        '''
        plugin = WSGI_Bottle()
        plugins['test'] = plugin
        app_mock = self.mocker.CreateMock(Bottle)
        def test_method():
            pass
        app_mock.route(path='/test', method='GET', callback=test_method, name=None)
        plugin.app = app_mock
        params = {'rule':'/test', 'method':'GET', 'target':test_method}
        self.mocker.ReplayAll()
        add_route('test', params)
        self.mocker.VerifyAll()