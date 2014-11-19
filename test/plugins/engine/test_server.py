#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bottle import *
from kokemomo.plugins.engine.controller.km_access_check import check_login

__author__ = 'hiroki'

app = default_app()
@app.route('/')
def index():
    return 'Hi!'

@app.route('/get_test')
@check_login(request, response)
def index():
    value = request.params.get('value')
    return value


if __name__ == '__main__':
    app.run()