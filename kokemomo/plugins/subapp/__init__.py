#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from kokemomo.lib.bottle import template, route, static_file, url


__author__ = 'hiroki'


@route('/subapp/js/<filename>', name='subapp_static_js')
def subapp_js_static(filename):
    """
    set javascript files.
    :param filename: javascript file name.
    :return: static path.
    """
    print("subapp static javascript load.")
    return static_file(filename, root='kokemomo/plugins/subapp/view/resource/js')


@route('/subapp/css/<filename>', name='subapp_static_css')
def subapp_css_static(filename):
    """
    set css files.
    :param filename: css file name.
    :return: static path.
    """
    return static_file(filename, root='kokemomo/plugins/subapp/view/resource/css')


@route('/subapp/img/<filename>', name='subapp_static_img')
def subapp_img_static(filename):
    """
    set image files.
    :param filename: image file name.
    :return: static path.
    """
    return static_file(filename, root='kokemomo/plugins/subapp/view/resource/img')


@route('/subapp')
def subapp():
    print("subapp load.")
    logging.info("subapp load")
    return template('kokemomo/plugins/subapp/view/sub_template', url=url) # TODO: パス解決を修正する

@route('/subapp/test')
def subapp_test():
    print("subapp test load.")
    logging.info("subapp test load")
    return template('kokemomo/plugins/subapp/view/sub_template', url=url) # TODO: パス解決を修正する