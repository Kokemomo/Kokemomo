#!/usr/bin/env python
# -*- coding: utf-8 -*-



import json

from kokemomo.plugins.engine.controller.km_plugin_manager import KMBaseController
from kokemomo.plugins.engine.controller.km_exception import log
from kokemomo.plugins.engine.controller.km_access_check import check_login
from kokemomo.plugins.engine.controller.km_login import logout, login_auth
from kokemomo.plugins.engine.utils.km_utils import get_menu_list

__author__ = 'hiroki'


class KMEngine(KMBaseController):


    def __init__(self):
        super(KMEngine, self).__init__('engine')
        self.add_route('/js/<filename>','GET', self.js_static, 'static_js')
        self.add_route('/css/<filename>','GET', self.css_static, 'static_css')
        self.add_route('/img/<filename>','GET', self.img_static, 'static_img')
        self.add_route('/login', 'GET', self.login)
        self.add_route('/login_auth', 'POST', self.login_auth)
        self.add_route('/index', 'GET', self.index)
        self.add_route('/error', 'GET', self.engine_error)


    @log
    def js_static(self, filename):
        """
        set javascript files.
        :param filename: javascript file name.
        :return: static path.
        """
        return self.load_static_file(filename, root='kokemomo/plugins/engine/view/resource/js')


    @log
    def css_static(self, filename):
        """
        set css files.
        :param filename: css file name.
        :return: static path.
        """
        return self.load_static_file(filename, root='kokemomo/plugins/engine/view/resource/css')


    @log
    def img_static(self, filename):
        """
        set image files.
        :param filename: image file name.
        :return: static path.
        """
        return self.load_static_file(filename, root='kokemomo/plugins/engine/view/resource/img')


    @log
    def index(self):
        menu_list = get_menu_list()
        user_id = self.data.get_user_id()
        return self.render('kokemomo/plugins/engine/view/index', url=self.get_url, user_id=user_id, type=type, menu_list=menu_list,)


    def engine_error(self):
        return "An error has occurred. Please contact the server administrator."


    def login(self):
        return self.render('kokemomo/plugins/engine/view/login', url=self.get_url)


    @log
    def login_auth(self):
        return login_auth(self.data)


    def logout(self):
        logout()
        return self.render('kokemomo/plugins/engine/view/login', url=self.get_url)


## User

#@route('/engine/user/save', method='POST')
@log
def save_user():
    pass

#@route('/engine/user/search')
@log
def search_user():
    pass

## Group

#@route('/engine/group/save', method='POST')
@log
def save_group():
    pass


#@route('/engine/group/search')
@log
def search_group():
    pass

## Role

#@route('/engine/role/save', method='POST')
@log
def save_role():
    pass


#@route('/engine/role/search')
@log
def search_role():
    pass


## Parameter

#@route('/engine/parameter/save', method='POST')
@log
def engine_save_parameter():
    pass


#@route('/engine/parameter/search', method='GET')
@log
def engine_search_parameter():
    pass
## File

#@route('/engine/file/upload', method='POST')
@log
def upload():
    pass

#@route('/engine/file/remove', method='POST')
@log
def remove_file():
    pass

#@route('/engine/file/change_dir', method="POST")
@log
def select_dir():
    pass