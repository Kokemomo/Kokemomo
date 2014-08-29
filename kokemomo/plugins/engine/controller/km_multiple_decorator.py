#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'hiroki'

import logging
import traceback


def multiple_decorator(*decorators):
    def _multiple_decorator(target_func):
            for d in reversed(decorators):
                target_func = d(target_func)
            return target_func
    return _multiple_decorator