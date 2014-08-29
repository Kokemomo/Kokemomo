#!/usr/bin/env python
# -*- coding:utf-8 -*-

from kokemomo.lib.bottle import request, get

__author__ = 'hiroki'

def add_session(request, user_id, value):
    session = request.environ.get('beaker.session')
    session[user_id] = value
    session.save()

def get_session(request, user_id):
    session = request.environ.get('beaker.session')
    return session[user_id]
