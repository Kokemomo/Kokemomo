#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kokemomo.lib.bottle import Bottle, run as runner
from kokemomo.lib.bottle import route, request, response, redirect, template, url
from kokemomo.lib.bottle import static_file, default_app

__author__ = 'hiroki-m'

'''

WSGIフレームワークのラッパークラスです。
各クラスの名前は「WSGI_フレームワーク名」にする必要があります。
※フレームワーク名はkokemomo.iniの「WSGI」セクションに設定した名前です。
例：
[WSGI]
name=Bottle

'''




class WSGI_Bottle:
    '''
    Bottleのラッパー
    '''

    root_app = default_app()

    @classmethod
    def get_root_app(cls):
        return cls.root_app

    @classmethod
    def set_root_app(cls, app):
        cls.root_app = app

    @classmethod
    def mount(cls, rule, plugin):
        cls.root_app.mount(rule, plugin.plugin.app)


    @classmethod
    def run(cls):
        if cls.root_app is not None:
            runner(cls.root_app, host='localhost', port=8861, debug=True, reloader=True)
        #        runner(app, host='localhost', port=8080, server='gunicorn', workers=1)
        else:
            raise SystemError


    def create_app(self):
        '''
        Bottleアプリケーションを生成します。
        '''
        self.app = Bottle()


    def add_route(self, params):
        '''
        Bottleアプリケーションに指定された情報でルーティングを追加します。
        ルーティングに必要な情報は以下の情報をディクショナリ形式で渡して下さい。
        rule: urlルール
        method: メソッド名
        target: 呼び出されるメソッドオブジェクト
        name: 名前（任意）

        :param params: ルーティングの情報
        '''
        rule = params['rule']
        method = params['method']
        target = params['target']
        if 'name' in params:
            name = params['name']
        else:
            name = None
        self.app.route(path=rule, method=method, callback=target, name=name);


    def get_request(self):
        return request


    def get_response(self):
        return response


    def get_reqeust_parameter(self, name, default):
        return request.params.get(name, default)


    def render(self, template_path, params):
        return template(template_path, params)


    def load_static_file(self, filename, root):
        return static_file(filename, root=root)