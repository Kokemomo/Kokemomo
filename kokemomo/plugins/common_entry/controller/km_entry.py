# #!/usr/bin/env python
# # -*- coding:utf-8 -*-

# from bottle import template, route, static_file, url, request
# from kokemomo.plugins.common_entry.controller.km_entry_config import get_model, get_name, entry_model
# from kokemomo.plugins.engine.utils.km_model_utils import *

# __author__ = 'hiroki'


# """
# This is the entry of generic functions.
# Use a model that has been set in km_entry_config.py.
# Generates display items of model set, it is possible to register a value.

# -------------------------------------------------------------------
# """

# from kokemomo.plugins.engine.model.km_storage import storage

# @route('/common_entry/js/<filename>', name='common_entry_static_js')
# def common_entry_js_static(filename):
#     """
#     set javascript files.
#     :param filename: javascript file name.
#     :return: static path.
#     """
#     return static_file(filename, root='kokemomo/plugins/common_entry/view/resource/js')


# @route('/common_entry/css/<filename>', name='common_entry_static_css')
# def common_entry_css_static(filename):
#     """
#     set css files.
#     :param filename: css file name.
#     :return: static path.
#     """
#     return static_file(filename, root='kokemomo/plugins/common_entry/view/resource/css')


# @route('/common_entry')
# def common_entry():
#     columns = get_columns()
#     title = get_title()
#     return template('kokemomo/plugins/common_entry/view/entry', url=url, title=title, columns=columns) # TODO: パス解決を修正する


# @route('/common_entry/save', method='POST')
# def common_entry_save():
#     entry(request)


# def get_columns():
#     """
#     return the columns.
#     :return:
#     """
#     return create_column_list(get_model())


# def get_title():
#     """
#     return the title.
#     :return:
#     """
#     return get_name()


# def entry(request):
#     """
#     to entry.
#     :param request:
#     :return:
#     """
#     for entry_params in request.forms:
#         model = set_value_list(get_model(), entry_params)
#         session = storage.adapter.session
#         entry_model(model, session)
#         session.close()
