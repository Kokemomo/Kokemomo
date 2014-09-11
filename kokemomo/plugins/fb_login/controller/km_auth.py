#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'hiroki'

import uuid

from kokemomo.lib.bottle import request
from kokemomo.plugins.engine.controller.km_session_manager import add_session


RESULT_SUCCESS = "SUCCESS"
RESULT_FAIL = "FAIL"


def create_session(request, response, id):
    result = RESULT_FAIL
    session_id = get_session_id()
    add_session(request, id, session_id)
    response.set_cookie('km_session', session_id) # TODO: セッション管理方法がこれで良いか再検討
    return result

def get_fb_code(session_id):
    session = request.environ.get('beaker.session')
    code = session_id in session
    return code

def get_session_id():
    return str(uuid.uuid1()) # TODO: セッションIDの生成方法を再検討
