#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kokemomo.lib.bottle import template, route, static_file, url

__author__ = 'hiroki'

@route('/application')
def application():
    return "<p>Call Application.</p>"