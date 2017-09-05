#!/usr/bin/env python
# -*- coding:utf-8 -*-
import bcrypt
from ..model.km_user_table import KMUser
from kokemomo.settings import SETTINGS
from .km_session_manager import add_value_to_session, delete_value_to_session, get_value_to_session


"""
It is a certification class for KOKEMOMO.

"""

__author__ = 'hiroki'


class KMLogin():

    RESULT_SUCCESS = "SUCCESS"
    RESULT_FAIL = "FAIL"

    # テスト用ユーザー
    test_user = "admin"
    test_password = "admin"
    test_user2 = "admin2"
    test_password2 = "admin2"

    @classmethod
    def logout(cls, km_data):
        request = km_data.get_request()
        cls.remove_session(request)


    @classmethod
    def login_auth(cls, km_data):
        for login_info in km_data.get_request().forms:
            login_args = login_info.split(':')
        result = cls.auth(
            km_data.get_request(), login_args[0], login_args[1])
        return result


    @classmethod
    def auth(cls, request, id, password):
        result = cls.RESULT_FAIL
        user = cls.get_user(id)
        if user is not None:
            enc_password = password.encode(SETTINGS.CHARACTER_SET)
            enc_user_password = user.password #.encode(SETTINGS.CHARACTER_SET)
            if bcrypt.hashpw(enc_password, enc_user_password) == enc_user_password:
                # create web_session
                result = cls.RESULT_SUCCESS

        # テスト用
        if SETTINGS.TEST_LOGIN == True:
            if id == cls.test_user and password == cls.test_password:
                result = cls.RESULT_SUCCESS
            if id == cls.test_user2 and password == cls.test_password2:
                result = cls.RESULT_SUCCESS

        if result == cls.RESULT_SUCCESS:
            cls.save_session(request, id)
        return result

    @classmethod
    def get_user(cls, user_id):
        users = KMUser.find(user_id=user_id)
        if len(users) == 0:
            return None
        return users[0]


    @classmethod
    def save_session(cls, request, id):
        add_value_to_session(request, 'user_id', id)


    @classmethod
    def remove_session(cls, request):
        delete_value_to_session(request, 'user_id')

    @classmethod
    def get_session(cls, request):
        return get_value_to_session(request, 'user_id')