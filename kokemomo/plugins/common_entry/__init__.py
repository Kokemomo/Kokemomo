#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kokemomo.lib.bottle import template, route, static_file, url, request, response, redirect
from kokemomo.plugins.common_entry.controller.km_entry import get_columns, get_title, entry

__author__ = 'hiroki'

@route('/common_entry/js/<filename>', name='common_entry_static_js')
def common_entry_js_static(filename):
    """
    set javascript files.
    :param filename: javascript file name.
    :return: static path.
    """
    return static_file(filename, root='kokemomo/plugins/common_entry/view/resource/js')


@route('/common_entry/css/<filename>', name='common_entry_static_css')
def common_entry_css_static(filename):
    """
    set css files.
    :param filename: css file name.
    :return: static path.
    """
    return static_file(filename, root='kokemomo/plugins/common_entry/view/resource/css')


@route('/common_entry')
def common_entry():
    columns = get_columns()
    title = get_title()
    return template('kokemomo/plugins/common_entry/view/entry', url=url, title=title, columns=columns) # TODO: パス解決を修正する

@route('/common_entry/save', method='POST')
def common_entry_save():
    entry(request)
