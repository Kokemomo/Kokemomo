#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kokemomo import app
from kokemomo.lib.bottle import template, route, static_file, url, request, response, redirect
from kokemomo.plugins.login.controller.km_user_manager import auth, RESULT_SUCCESS
from bottle.ext import auth
from bottle.ext.auth.decorator import login
from bottle.ext.auth.social.facebook import Facebook, UserDenied
from bottle.ext.auth.social.facebook import NegotiationError
from pprint import pformat
from bottle_auth.core.auth import FacebookGraphMixin, HTTPRedirect
from urllib2 import Request,urlopen
import logging
from kokemomo.plugins.fb_login.controller.km_auth import create_session, RESULT_FAIL, RESULT_SUCCESS, get_fb_code
import os

__author__ = 'hiroki'


"""
This is the login screen of the Facebook login.

"""

CLIENT_ID = 'app-id' # TODO: 設定ファイルへ抜き出し
REDIRECT_URI='redirect-uri'
SECRET_KEY = 'secret-key'
EMAIL = 'e-mail'
DATA_DIR_PATH = "./kokemomo/data/test/"# TODO: 実行する場所によって変わる為、外部ファイルでHOMEを定義するような仕組みへ修正する

facebook = Facebook(CLIENT_ID, SECRET_KEY,
                    REDIRECT_URI, EMAIL)

plugin = auth.AuthPlugin(facebook)
app.install(plugin)


#logging.basicConfig(filename='login.log', level=logging.INFO)

@route('/fb_login/js/<filename>', name='fb_login_static_js')
def fb_login_js_static(filename):
    """
    set javascript files.
    :param filename: javascript file name.
    :return: static path.
    """
    return static_file(filename, root='kokemomo/plugins/fb_login/view/resource/js')


@route('/fb_login/css/<filename>', name='fb_login_static_css')
def fb_login_css_static(filename):
    """
    set css files.
    :param filename: css file name.
    :return: static path.
    """
    return static_file(filename, root='kokemomo/plugins/fb_login/view/resource/css')


@route('/fb_login/img/<filename>', name='fb_login_static_img')
def fb_login_img_static(filename):
    """
    set image files.
    :param filename: image file name.
    :return: static path.
    """
    return static_file(filename, root='kokemomo/plugins/fb_login/view/resource/img')

@app.route('/fb_login')
def fb_login_top(auth):
    return template('kokemomo/plugins/fb_login/view/login', url=url) # TODO: パス解決を修正する

@app.route('/fb_login_auth')
def fb_login_auth():
    auth = FacebookGraphMixin(request.environ)
    try:
        auth.authorize_redirect(
            redirect_uri=facebook.callback_url,
            client_id=facebook.settings['facebook_api_key'])
#            extra_params={'scope': facebook.scope}) # TODO: 現状scopeにEMAILが入りスコープエラーとなるため、bottle-authのバグかどうか要調査
    except HTTPRedirect, e:
        logging.info('Redirecting Facebook user to {0}'.format(e.url))
        return redirect(e.url)
    return None

@app.route('/fb_engine/<filename>')
def fb_engine(filename):
    # TODO: 認証処理などはcontrollerへ移動
    auth = FacebookGraphMixin(request.environ)
    container = {}
    try:
        code = request.params['code']
    except KeyError as e:
        return "<p>Please login!</p>" # TODO: 例外スロー時にエラー画面に遷移するようにする
    result = RESULT_FAIL
    if code is '':
        km_session_key = request.get_cookie('km_session_id') # TODO: 現状としてログイン後の画面へのURLを直接たたくとアクセスできないため対応が必要
        code = get_fb_code(km_session_key)
    code = str(code) + '#_=_'
    def get_user_callback(user):
        container['id'] = user['id']

    auth.get_authenticated_user(
        redirect_uri=facebook.callback_url,
        client_id=facebook.settings['facebook_api_key'],
        client_secret=facebook.settings['facebook_secret'],
        code=code,
        callback=get_user_callback)

    if container['id'] is not '':
        create_session(request, response, container['id'])
        result = RESULT_SUCCESS

    if result is RESULT_FAIL: # TODO: チェック処理とページ遷移の処理を統一化する必要がある（通常ログインの場合とFacebookログインの場合）
        return "<p>Please login!</p>" # TODO: 例外スロー時にエラー画面に遷移するようにする
    if filename == "file":
        dir_list = []
        for (root, dirs, files) in os.walk(DATA_DIR_PATH):
            for dir_name in dirs:
                dir_path = root + os.sep + dir_name
                dir_list.append(dir_path[len(DATA_DIR_PATH):])
        files = os.listdir(DATA_DIR_PATH + dir_list[0])
        files = os.listdir(DATA_DIR_PATH + dir_list[0])
        for file_name in files:
            if os.path.isdir(DATA_DIR_PATH + os.sep + dir_list[0] + os.sep + file_name):
                files.remove(file_name)
        return template('kokemomo/plugins/engine/view/file', dirs=dir_list, files=files, url=url) # TODO: パス解決を改修
    else:
        return template('kokemomo/plugins/engine/view/' + filename, url=url) # TODO: パス解決を改修
