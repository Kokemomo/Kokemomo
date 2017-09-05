#!/usr/bin/env python
# -*- coding:utf-8 -*-

from functools import wraps

from kokemomo.settings import SETTINGS
from kokemomo.plugins.engine.model.km_user_table import KMUser
from kokemomo.plugins.engine.model.km_group_table import KMGroup
from kokemomo.plugins.engine.model.km_role_table import KMRole
from .km_session_manager import get_value_to_session


"""
Access check class for KOKEMOMO.

It provides as a decorator each check processing.

"""

__author__ = 'hiroki'

from kokemomo.plugins.engine.model.km_storage import storage


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
                user = KMUser.get(user_id)
                user_id = user.id
                role = KMRole(user_id)
                if check_target(request, role):
                    return callback(*args, **kwargs)
                else:
                    # TODO: 例外スロー時にエラー画面に遷移するようにする
                    return "<p>Access is not allowed!</p>"
        return wrapper
    return _access_check


def check_target(request, role):
    paths = request.path.split('/')
    path = '/' + paths[1]
    is_target = False
    size = len(paths)
    if size > 1 and role.target == path:  # application scope
        is_target = True
    # function scope
    elif size > 3 and role.target == '/'.join([path, paths[2]]):
        is_target = True
    # sub function scope
    elif size > 5 and role.target == '/'.join([path, paths[2], paths[3]]):
        is_target = True
    if is_target and not role.is_allow:
        return False
    return True

