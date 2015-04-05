#!/usr/bin/env python
# -*- coding:utf-8 -*-

from kokemomo.plugins.engine.utils.km_config import get_character_set_setting, get_admin_menu_setting
from kokemomo.plugins.engine.controller.km_menu import KMMenu

__author__ = 'hiroki'

def create_result(data):
    """
    The conversion to the format of the JSON string in a string that has been specified.
    "result" is the key.
    """
    result = '{"result":"' + data + '"}' # TODO: modelの場合はget_jsonを使うようにする
    return result

def create_result_4_array(list):
    """
    The conversion to the format of the JSON string the specified array
    "result" is the key.
    """
    result = ""
    for data in list:
        result = result + data.get_json() + ","
    print(result)
    result = '{"result":[' + result[0:-1] + ']}'
    return result

def get_menu_list():
    list = []
    menu_params = get_admin_menu_setting()['menu']
    for menu in menu_params:
        item = KMMenu()
        item.name = menu
        item.url = menu_params[menu]
        list.append(item)
    return list

