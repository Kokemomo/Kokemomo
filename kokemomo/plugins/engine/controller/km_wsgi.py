#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kokemomo.lib.bottle import Bottle

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
