#!/usr/bin/env python
# -*- coding:utf-8 -*-

import uuid

from kokemomo.plugins.engine.model.km_user_table import get_session, find
from kokemomo.plugins.engine.controller.km_session_manager import add_session

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


def auth(request, response, id, password):
    result = RESULT_FAIL
    session = get_session()
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
