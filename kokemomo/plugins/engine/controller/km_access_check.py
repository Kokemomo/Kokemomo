#!/usr/bin/env python
# -*- coding:utf-8 -*-

from functools import wraps
from xml.sax.saxutils import *
from kokemomo.lib.bottle import redirect
from kokemomo.plugins.engine.model.km_user_table import find as find_user
from kokemomo.plugins.engine.model.km_role_table import find as find_role
from kokemomo.plugins.engine.controller.km_session_manager import get_value_to_session
from kokemomo.plugins.engine.controller.km_db_manager import *
from kokemomo.plugins.engine.utils.km_config import get_character_set_setting

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
            user_id = get_value_to_session(request, 'user_id')
            if user_id is not None:
                try:
                    session = db_manager.get_session()
                    user = find_user(user_id, session)
                    user_id = user.id
                    role = find_role(user_id, session)
                    if check_target(request, role):
                        return callback(*args, **kwargs)
                    else:
                        return "<p>Access is not allowed!</p>" # TODO: 例外スロー時にエラー画面に遷移するようにする
                finally:
                    session.close()
        return wrapper
    return _access_check


def check_target(request, role):
    paths = request.path.split('/')
    path = '/' + paths[1]
    is_target = False
    if len(paths) > 1 and role.target == path: # application scope
        is_target = True
    elif len(paths) > 3 and role.target == (path + '/' + paths[2]): # function scope
        is_target = True
    elif len(paths) > 5 and role.target == (path + '/' + paths[2] + '/' + paths[3]): # sub function scope
        is_target = True
    if is_target and not role.is_allow:
        return False
    return True


def check_login(request, response):
    """
    Check to see if it is logged.
    :param request:var ui = HtmlService.createHtmlOutputFromFile('sidebar')
      .setTitle('sidebar');

    :return:
    """
    def _check_login(callback):
        @wraps(callback)
        def wrapper(*args, **kwargs):
            response.set_header("Content-Type", "text/html; charset=" + get_character_set_setting())
            user_id = get_value_to_session(request, 'user_id')
            if user_id is not None:
                return callback(*args, **kwargs)
            return redirect('/engine/login?errorcode=0')
        return wrapper
    return _check_login

