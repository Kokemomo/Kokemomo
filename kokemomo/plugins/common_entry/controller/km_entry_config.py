#!/usr/bin/env python
# -*- coding:utf-8 -*-

from kokemomo.plugins.engine.model.km_user_table import KMUser, get_session, add

__author__ = 'hiroki'

"""
Set a model that entry here.
Set the user model as a sample.

-------------------------------------------------------------------
"""

def get_model():
    """
    return the model.
    :return:
    """
    return KMUser()

def get_name():
    """
    return the name.
    :return:
    """
    return "ユーザー登録"

def entry_model(model):
    """
    entry model.
    :param model:
    :return:
    """
    session = get_session()
    add(model, session)
    session.close()
