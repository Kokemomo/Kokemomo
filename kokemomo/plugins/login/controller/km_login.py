#!/usr/bin/env python
# -*- coding:utf-8 -*-

import uuid

from kokemomo.lib.bottle import template, route, static_file, url, request, response, redirect
from kokemomo.plugins.engine.model.km_user_table import find
from kokemomo.plugins.engine.controller.km_session_manager import add_session
from kokemomo.plugins.engine.controller.km_db_manager import *
from kokemomo.plugins.engine.controller.km_exception import log

"""
It is a certification class for KOKEMOMO.

"""

__author__ = 'hiroki'

RESULT_SUCCESS = "SUCCESS"
RESULT_FAIL = "FAIL"

# テスト用ユーザー
test_user = "admin"
test_password = "admin"
test_user2 = "admin2"
test_password2 = "admin2"

db_manager = KMDBManager("engine")


@route('/login/js/<filename>', name='login_static_js')
def login_js_static(filename):
    """
    set javascript files.
    :param filename: javascript file name.
    :return: static path.
    """
    return static_file(filename, root='kokemomo/plugins/login/view/resource/js')


@route('/login/css/<filename>', name='login_static_css')
def login_css_static(filename):
    """
    set css files.
    :param filename: css file name.
    :return: static path.
    """
    return static_file(filename, root='kokemomo/plugins/login/view/resource/css')


@route('/login/img/<filename>', name='login_static_img')
def login_img_static(filename):
    """
    set image files.
    :param filename: image file name.
    :return: static path.
    """
    return static_file(filename, root='kokemomo/plugins/login/view/resource/img')


@route('/login')
def login():
    print("login load.")
    return template('kokemomo/plugins/login/view/login', url=url) # TODO: パス解決を修正する


@route('/login/auth', method='POST')
@log
def login_auth():
    for login_info in request.forms:
        login_args = login_info.split(':')
        print(login_args)
    result = auth(request, response, login_args[0], login_args[1])
    return result



def auth(request, response, id, password):
    result = RESULT_FAIL
    session = db_manager.get_session()
    user = find(id, session)
    if user is not None:
        user_password = user.password
        if user_password is password:
            # create web_session
            print("authenticate success!")
            result = RESULT_SUCCESS

    # テスト用
    if id == test_user and password == test_password:
        result = RESULT_SUCCESS
    if id == test_user2 and password == test_password2:
        result = RESULT_SUCCESS

    if result == RESULT_SUCCESS:
        session_id = get_session_id()
        add_session(request, id, session_id)
    session.close()
    return result

def get_session_id():
    return str(uuid.uuid1())
