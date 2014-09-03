#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Contents Management System KOKEMOMO

"""
import os
import logging
import json

from beaker.middleware import SessionMiddleware

from kokemomo.lib.bottle import route, run as runner, request, response, redirect, template, get, url
from kokemomo.lib.bottle import static_file, default_app
from kokemomo.plugins.engine.model.km_parameter_table import get_session, find_all, delete, update
from kokemomo.plugins.engine.utils.km_utils import create_result, create_result_4_array
from kokemomo.plugins.engine.controller.km_exception import log, KMException
from kokemomo.plugins.login.controller.km_access_check import check_login
from kokemomo.plugins.engine.model.km_user_table import get_session as user_get_session, find_all as user_find_all, delete as user_delete, update as user_update


#from kokemomo.plugins.engine.utils.km_auth import auth

from kokemomo.plugins.login import login
from kokemomo.plugins import subapp
import application

logging.basicConfig(filename='engine.log', level=logging.INFO, format='%(asctime)s %(message)s')

# session config
session_opts = {
    'session.type': 'file',
    'session.data_dir': './session_data',
    'session.cookie_expires': True,
    'session.auto': True
}

# sub subapp mount
app = default_app()
from kokemomo.plugins import fb_login
app.mount('/subapp', subapp)
app.mount('/login', login)
app.mount('/fb-login', fb_login)
app.mount('/application', application)
app = SessionMiddleware(app, session_opts)

DATA_DIR_PATH = "./kokemomo/data/test/"# TODO: 実行する場所によって変わる為、外部ファイルでHOMEを定義するような仕組みへ修正する
VERSION = "0.5.0"
print("KOKEMOMO ver." + VERSION)


@route('/')
@log
def top():
    """
    redirect to /engine url.
    """
    redirect('/engine')


@route('/engine/js/<filename>', name='static_js')
@log
def js_static(filename):
    """
    set javascript files.
    :param filename: javascript file name.
    :return: static path.
    """
    return static_file(filename, root='kokemomo/plugins/engine/view/resource/js')


@route('/engine/css/<filename>', name='static_css')
@log
def css_static(filename):
    """
    set css files.
    :param filename: css file name.
    :return: static path.
    """
    return static_file(filename, root='kokemomo/plugins/engine/view/resource/css')


@route('/engine/img/<filename>', name='static_img')
@log
def img_static(filename):
    """
    set image files.
    :param filename: image file name.
    :return: static path.
    """
    return static_file(filename, root='kokemomo/plugins/engine/view/resource/img')


#@route('/engine/template/<filename>', name='static_template')
#def template_static(filename):
#    return static_file(filename, root='kokemomo/templates/engine/', url=url)


@route('/engine')
@log
@check_login(request)
def load():
    return template('kokemomo/plugins/engine/view/admin', url=url) # TODO: パス解決を改修

@route('/engine/file/change_dir', method="POST")
@log
def select_dir():
    """
    Return the directory list for designated.

    example: If there is a dir1, dir2, dir3 in ". /data/(dir※)" directly under.
    ※Directory that is specified in the form.

    :return: "dir1,dir2,dir3"
    """
    dirs = os.listdir(DATA_DIR_PATH)
    # dir only
    for dir_name in dirs:
        if os.path.isfile(dir_name):
            dirs.remove(dir_name)
    files = []
    for selectDir in request.forms:
        files = os.listdir(DATA_DIR_PATH + os.sep + selectDir)
    result = ""
    for file_name in files:
        if not file_name.startswith("."):
            result = result + file_name + ","
    result = result[0:len(result) - 1]
    return create_result(result)


@route('/engine/parameter/save', method='POST')
@log
def save_parameter():
    """
    Save the parameter.
    will save the json string in the following formats.
    Format: 'keyName':{"hoge":"fuga"}

    """
    session = get_session()
    for save_params in request.forms:
        json_data = json.loads(save_params.decode('utf-8'))
        for key in json_data:
            if json_data[key] == "":
                delete(key, session)  # delete
            else:
                update(key, json_data[key], session)
    session.close()


@route('/engine/parameter/search', method='GET')
@log
def search_parameter():
    """
    Find all the parameters.
    :return: parameters.
    """
    session = get_session()
    result = find_all(session)
    session.close()
    return create_result_4_array(result)


@route('/engine/file/upload', method='POST')
@log
def upload():
    """
    Save the file that is specified in the request.
    """
    directory_path = request.forms.get('directory').decode('utf-8')
    data = request.files
    file_obj = data.get('files')
    file_name = file_obj.filename
    file_name = file_name.decode('utf-8')
    save_path = os.path.join(DATA_DIR_PATH + os.sep + directory_path, file_name)
    with open(save_path, "wb") as open_file:
        open_file.write(file_obj.file.read())
        logging.info("file upload. name=" + save_path);
    redirect("/engine")


@route('/engine/file/remove', method='POST')
@log
def remove_file():
    """
    Remove the file.
    """
    for remove_target in request.forms:
        target = remove_target.split(',')
        os.remove(DATA_DIR_PATH + os.sep + target[0] + os.sep + target[1])
        print("remove. " + DATA_DIR_PATH + os.sep + target[0] + os.sep + target[1])


@route('/engine/user/save', method='POST')
@log
def save_user():
    """
    Save the user.
    will save the json string in the following formats.
    Format: 'keyName':{"hoge":"fuga"}

    """
    session = user_get_session()
    for save_user in request.forms:
        json_data = json.loads(save_user.decode('utf-8'))
        for id in json_data:
            if json_data[id] == "":
                user_delete(id, session)  # delete
            else:
                user_update(id, "", json_data[id], "", 0, "", session)
    session.close()


@route('/engine/user/search')
@log
def search_user():
    """
    Find all the user.
    :return: users.
    """
    session = user_get_session()
    result = user_find_all(session)
    session.close()
    return create_result_4_array(result)

@route('/engine/<filename>')
@log
@check_login(request)
def load_admin(filename):
    if filename == "file":
        dir_list = []
        for (root, dirs, files) in os.walk(DATA_DIR_PATH):
            for dir_name in dirs:
                dir_path = root + os.sep + dir_name
                dir_list.append(dir_path[len(DATA_DIR_PATH):])
        files = os.listdir(DATA_DIR_PATH + dir_list[0])
        files = os.listdir(DATA_DIR_PATH + dir_list[0])
        for file_name in files:
            if os.path.isdir(DATA_DIR_PATH + os.sep + dir_list[0] + os.sep + file_name):
                files.remove(file_name)
        return template('kokemomo/plugins/engine/view/file', dirs=dir_list, files=files, url=url) # TODO: パス解決を改修
    else:
        return template('kokemomo/plugins/engine/view/' + filename, url=url) # TODO: パス解決を改修


def app_run():
        if app is not None:
            runner(app, host='localhost', port=8861, debug=True, reloader=True)
    #        runner(app, host='localhost', port=8080, server='gunicorn', workers=1)
        else:
            raise SystemError
