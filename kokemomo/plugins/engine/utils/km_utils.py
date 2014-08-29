#!/usr/bin/env python
# -*- coding:utf-8 -*-

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
