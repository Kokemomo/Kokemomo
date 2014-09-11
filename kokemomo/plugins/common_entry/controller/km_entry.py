#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
from kokemomo.plugins.common_entry.controller.km_entry_config import get_model, get_name, entry_model
from kokemomo.plugins.engine.utils.km_model_utils import *

__author__ = 'hiroki'

"""
This is the entry of generic functions.
Use a model that has been set in km_entry_config.py.
Generates display items of model set, it is possible to register a value.

-------------------------------------------------------------------
"""
def get_columns():
    """
    return the columns.
    :return:
    """
    return create_column_list(get_model())

def get_title():
    """
    return the title.
    :return:
    """
    return get_name()

def entry(request):
    """
    to entry.
    :param request:
    :return:
    """
    for entry_params in request.forms:
        model = set_value_list(get_model(), entry_params)
        entry_model(model)