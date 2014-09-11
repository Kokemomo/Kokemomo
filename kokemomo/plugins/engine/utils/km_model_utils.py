#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy.schema import Column
from sqlalchemy import create_engine, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from types import *
import datetime
import inspect
import json
from abc import ABCMeta, abstractmethod

__author__ = 'hiroki'


"""
-------------------------------------------------------------------
"""

def create_repr_str(model):
    result = '<' + model.__class__.__name__ + '('
    for column in model.__table__.c:
        value = getattr(model, column.name)
        if value is None:
            value = ''
        result += (column.name + '="' + str(value) + '",')
    result = result[0:-1] + ')>'
    return result

def create_json(model):
    result = '{'
    for column in model.__table__.c:
        value = getattr(model, column.name)
        if value is not None:
            try:
                # json形式の値の場合はダブルクォートをつけない
                json.loads(str(value))
                result += ('"' + column.name + '":' + str(value) + ',')
            except ValueError as ve:
                result += ('"' + column.name + '":"' + str(value) + '",')
    result = result[0:-1] + '}'
    return result

def create_column_list(model):
    columns = []
    for column in model.__table__.c:
        if column.name is not "create_at" and column.name is not "update_at":
            columns.append(column.name)
    return columns


def create_value_list(model):
    value_list = []
    for column in model.__table__.c:
        value = getattr(model, column.name)
        value_list[column] = value
    return value_list

def set_value_list(model, json_str):
    json_data = json.loads(json_str.decode('utf-8'))
    for key in json_data:
        setattr(model, key, str(json_data[key])) # TODO: 項目のタイプによって型を変換する
    return model