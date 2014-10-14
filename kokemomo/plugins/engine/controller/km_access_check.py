#!/usr/bin/env python
# -*- coding:utf-8 -*-

from functools import wraps
from kokemomo.plugins.engine.model.km_user_table import find as find_user
from kokemomo.plugins.engine.model.km_role_table import find as find_role
from kokemomo.plugins.engine.controller.km_db_manager import *

"""
Access check class for KOKEMOMO.

It provides as a decorator each check processing.

"""

__author__ = 'hiroki'

db_manager = KMDBManager("engine")

def access_check(request):
    """
    Check to see if you can access to the target page.
    :param request:
    :return:
    """
    def _access_check(callback):
        @wraps(callback)
        def wrapper(*args, **kwargs):
            if hasattr(request, "cookies"):
                user_id = request.cookies.user_id
                if user_id is not u'':
                    session = db_manager.get_session()
                    user = find_user(user_id, session)
                    user_id = user.id
                    session.close()
                    session = db_manager.get_session()
                    role = find_role(user_id, session)
                    session.close()
                    if check_target(request, role):
                        return callback(*args, **kwargs)
                    else:
                        return "<p>Access is not allowed!</p>" # TODO: 例外スロー時にエラー画面に遷移するようにする
        return wrapper
    return _access_check


def check_target(request, role):
    pass # TODO: ロールのtargetとURLのチェック処理の実装


def check_login(request):
    """
    Check to see if it is logged.
    :param request:var ui = HtmlService.createHtmlOutputFromFile('sidebar')
      .setTitle('sidebar');

    :return:
    """
    def _check_login(callback):
        @wraps(callback)
        def wrapper(*args, **kwargs):
            if hasattr(request, "cookies"):
                user_id = request.cookies.user_id
                session = request.environ.get('beaker.session')
                if user_id is not u'' or session is not None:
                    login_info = user_id in session
                    if login_info:
                        return callback(*args, **kwargs)
                return "<p>Not Logged!</p>" # TODO: 例外スロー時にエラー画面に遷移するようにする
        return wrapper
    return _check_login

