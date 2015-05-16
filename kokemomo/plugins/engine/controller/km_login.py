#!/usr/bin/env python
# -*- coding:utf-8 -*-

import uuid

from kokemomo.lib.bottle import template, route, static_file, url, request, response, redirect
from kokemomo.plugins.engine.model.km_user_table import find
from kokemomo.plugins.engine.controller.km_session_manager import add_value_to_session, delete_value_to_session
from kokemomo.plugins.engine.controller.km_db_manager import *
from kokemomo.plugins.engine.controller.km_exception import log
from kokemomo.plugins.engine.utils.km_config import get_test_setting


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

test_login = get_test_setting()['test_login']

db_manager = KMDBManager("engine")

#@route('/engine/login')
def login():
    return template('kokemomo/plugins/engine/view/login', url=url)


@route('/engine/login/auth', method='POST')
@log
def login_auth():
    for login_info in request.forms:
        login_args = login_info.split(':')
    result = auth(request, response, login_args[0], login_args[1])
    return result


@route('/engine/logout')
@log
def logout():
    delete_value_to_session(request, 'user_id')
    return template('kokemomo/plugins/engine/view/login', url=url)


def auth(request, response, id, password):
    result = RESULT_FAIL
    try:
        session = db_manager.get_session()
        user = find(id, session)
        if user is not None:
            user_password = user.password
            if user_password == password:
                # create web_session
                result = RESULT_SUCCESS

        # テスト用
        if test_login == 'true':
            if id == test_user and password == test_password:
                result = RESULT_SUCCESS
            if id == test_user2 and password == test_password2:
                result = RESULT_SUCCESS

        if result == RESULT_SUCCESS:
            add_value_to_session(request, 'user_id', id)
    finally:
        session.close()
    return result
