#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..model.km_user_table import find
from ..utils.km_config import get_test_setting
from .km_session_manager import add_value_to_session, delete_value_to_session


"""
It is a certification class for KOKEMOMO.

"""

__author__ = 'hiroki'


# TODO authインターフェースへ変更
# TODO ユーザーの取得などはモデルへ移行
# TODO セッションマネージャ関連もラップできないか検討


RESULT_SUCCESS = "SUCCESS"
RESULT_FAIL = "FAIL"

# テスト用ユーザー
test_user = "admin"
test_password = "admin"
test_user2 = "admin2"
test_password2 = "admin2"

test_login = get_test_setting()['test_login']


def logout(data):
    request = data.get_request()
    delete_value_to_session(request, 'user_id')


def login_auth(km_data, db_manager):
    for login_info in km_data.get_request().forms:
        login_args = login_info.split(':')
    result = auth(
        km_data.get_request(), db_manager, login_args[0], login_args[1])
    return result


def auth(request, db_manager, id, password):
    result = RESULT_FAIL
    try:
        session = db_manager.adapter.session
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
