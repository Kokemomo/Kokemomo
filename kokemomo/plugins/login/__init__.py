#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kokemomo.lib.bottle import template, route, static_file, url, request, response, redirect
from kokemomo.plugins.login.controller.km_user_manager import auth, RESULT_SUCCESS
from kokemomo.plugins.engine.controller.km_exception import log

__author__ = 's.hirota'

#logging.basicConfig(filename='login.log', level=logging.INFO)

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
