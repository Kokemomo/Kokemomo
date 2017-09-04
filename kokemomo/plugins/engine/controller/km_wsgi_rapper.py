#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, run as runner, Route
from bottle import request, response, redirect, template
from bottle import static_file, default_app
from kokemomo.settings import SETTINGS

__author__ = 'hiroki-m'

'''

WSGIフレームワークのラッパークラスです。
各クラスの名前は「WSGI_フレームワーク名」にする必要があります。
※フレームワーク名はkokemomo.iniの「WSGI」セクションに設定した名前です。
例：
[WSGI]
name=Bottle

'''


class WSGI_Bottle:  # TODO WSGI_Rapperインターフェースを作って実装はファイルを分けよう

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
    def run(cls, port):
        if cls.root_app is not None:
            runner(cls.root_app, host='localhost',
               port=port, debug=SETTINGS.DEBUG, reloader=SETTINGS.RELOAD)
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
#        route = Route(self.app, rule, method, target)
#        self.app.add_route(route)
        self.app.route(path=rule, method=method, callback=target, name=name)

    def get_request(self):  # TODO static変数へのアクセスなのでクラスメソッドにするべきか？
        return request

    def get_response(self):  # TODO static変数へのアクセスなのでクラスメソッドにするべきか？
        return response

    # TODO static変数へのアクセスなのでクラスメソッドにするべきか？
    def get_request_parameter(self, name, default):
        return request.params.getunicode(name, default)
        
    # TODO static変数へのアクセスなのでクラスメソッドにするべきか？
    def render(self, template_path, params):
        return template(template_path, params)

    # TODO static変数へのアクセスなのでクラスメソッドにするべきか？
    def load_static_file(self, filename, root):
        return static_file(filename, root=root)

    def redirect(self, url, code):  # TODO static変数へのアクセスなのでクラスメソッドにするべきか？
        redirect(url, code)
