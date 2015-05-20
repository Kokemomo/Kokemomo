#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'hiroki'


def add_value_to_session(request, key, value):
    '''
    add session value.
    :param request: bottle session object.
    :param key: key.
    :param value: value.
    :return:
    '''
    session = request.environ.get('beaker.session')
    session[key] = value
    session.save()


def get_value_to_session(request, key):
    '''
    get session value.
    :param request: bottle request object.
    :param key: key.
    :return:
    '''
    session = request.environ.get('beaker.session')
    result = None
    if key in session:
        result = session[key]
    return result


def delete_value_to_session(request, key):
    '''
    delete session value.
    :param request: bottle request object.
    :param key: key.
    :return:
    '''
    session = request.environ.get('beaker.session')
    session[key] = None
    session.save()
