#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, json
from kokemomo.lib.bottle import route, request, response, redirect, template, url
from kokemomo.lib.bottle import static_file

from kokemomo.plugins.engine.controller.km_db_manager import *
from kokemomo.plugins.engine.controller.km_session_manager import get_value_to_session
from kokemomo.plugins.engine.model.km_user_table import find_all as user_find_all, delete as user_delete, update as user_update, KMUser
from kokemomo.plugins.engine.model.km_group_table import find_all as group_find_all, delete as group_delete, update as group_update, KMGroup
from kokemomo.plugins.engine.model.km_role_table import find_all as role_find_all, delete as role_delete, update as role_update, KMRole
from kokemomo.plugins.engine.model.km_parameter_table import find_all as find_parameter, delete as delete_parameter, update as update_parameter, KMParameter

from kokemomo.plugins.engine.utils.km_config import get_character_set_setting
from kokemomo.plugins.engine.utils.km_utils import get_menu_list
from kokemomo.plugins.engine.utils.km_utils import create_result, create_result_4_array

DATA_DIR_PATH = "./kokemomo/data/test/"# TODO: 実行する場所によって変わる為、外部ファイルでHOMEを定義するような仕組みへ修正する

charset = get_character_set_setting()


__author__ = 'hiroki-m'


db_manager = KMDBManager("engine")


def index():
    type = request.params.get('type', default='info')
    user_id = get_value_to_session(request, 'user_id')
    dirs = []
    files = []
    if type == "file":
        for (root, dir_list, files) in os.walk(DATA_DIR_PATH):
            for dir_name in dir_list:
                dir_path = root + os.sep + dir_name
                dirs.append(dir_path[len(DATA_DIR_PATH):])
        files = os.listdir(DATA_DIR_PATH + dirs[0])
        for file_name in files:
            if os.path.isdir(DATA_DIR_PATH + os.sep + dirs[0] + os.sep + file_name):
                files.remove(file_name)
    menu_list = get_menu_list()
    return template('kokemomo/plugins/engine/view/' + type, url=url, user_id=user_id, type=type, menu_list=menu_list, dirs=dirs, files=files) # TODO: パス解決を改修



def save_user():
    """
    Save the user.
    will save the json string in the following formats.
    Format: 'keyName':{"hoge":"fuga"}

    """
    try:
        session = db_manager.get_session()
        for save_user in request.forms:
            json_data = json.loads(save_user.decode(charset))
            for id in json_data:
                if json_data[id] == "":
                    user_delete(id, session)  # delete
                else:
                    user = KMUser()
                    user.user_id = json_data[id]['user_id']
                    user.name = json_data[id]["name"]
                    user.password = json_data[id]["password"]
                    user.mail_address = json_data[id]["mail_address"]
                    user.group_id = json_data[id]["group_id"]
                    user.role_id = json_data[id]["role_id"]
                    user_update(user, session)
    finally:
        session.close()


def search_user():
    """
    Find all the user.
    :return: users.
    """
    try:
        session = db_manager.get_session()
        result = user_find_all(session)
    finally:
        session.close()
    return create_result_4_array(result)


def save_group():
    """
    Save the Group.
    will save the json string in the following formats.
    Format: 'keyName':{"hoge":"fuga"}

    """
    try:
        session = db_manager.get_session()
        for save_group in request.forms:
            json_data = json.loads(save_group.decode(charset))
            for id in json_data:
                if json_data[id] == "":
                    group_delete(id, session)  # delete
                else:
                    group = KMGroup()
                    group.name = json_data[id]["name"]
                    group.parent_id = json_data[id]["parent_id"]
                    group_update(group, session)
    finally:
        session.close()


def search_group():
    """
    Find all the group.
    :return: groups.
    """
    try:
        session = db_manager.get_session()
        result = group_find_all(session)
    finally:
        session.close()
    return create_result_4_array(result)



def save_role():
    """
    Save the role.
    will save the json string in the following formats.
    Format: 'keyName':{"hoge":"fuga"}

    """
    try:
        session = db_manager.get_session()
        for save_group in request.forms:
            json_data = json.loads(save_group.decode(charset))
            for id in json_data:
                if json_data[id] == "":
                    role_delete(id, session)  # delete
                else:
                    role = KMRole()
                    role.id = id
                    role.name = json_data[id]["name"]
                    role.target = json_data[id]["target"]
                    role.is_allow = json_data[id]["is_allow"]
                    role_update(role, session)
    finally:
        session.close()




def search_role():
    """
    Find all the role.
    :return: roles.
    """
    try:
        session = db_manager.get_session()
        result = role_find_all(session)
    finally:
        session.close()
    return create_result_4_array(result)



def engine_save_parameter():
    """
    Save the parameter.
    will save the json string in the following formats.
    Format: 'keyName':{"hoge":"fuga"}

    """
    try:
        session = db_manager.get_session()
        for save_params in request.forms:
            json_data = json.loads(save_params.decode(charset))
            for key in json_data:
                if json_data[key] == "":
                    delete_parameter(key, session)  # delete
                else:
                    parameter = KMParameter()
                    parameter.key = key
                    parameter.json = json_data[key]
                    update_parameter(parameter, session)
    finally:
        session.commit()


def engine_search_parameter():
    """
    Find all the parameters.
    :return: parameters.
    """
    try:
        session = db_manager.get_session()
        result = find_parameter(session)
    finally:
        session.commit()
    return create_result_4_array(result)


def upload():
    """
    Save the file that is specified in the request.
    """
    directory_path = request.forms.get('directory').decode(charset)
    data = request.files
    file_obj = data.get('files')
    file_name = file_obj.filename
    file_name = file_name.decode(charset)
    save_path = os.path.join(DATA_DIR_PATH + os.sep + directory_path, file_name)
    with open(save_path, "wb") as open_file:
        open_file.write(file_obj.file.read())
#        logging.info("file upload. name=" + save_path);
    redirect("/engine/top")


def remove_file():
    """
    Remove the file.
    """
    for remove_target in request.forms:
        target = remove_target.split(',')
        os.remove(DATA_DIR_PATH + os.sep + target[0] + os.sep + target[1])
        print("remove. " + DATA_DIR_PATH + os.sep + target[0] + os.sep + target[1])


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
