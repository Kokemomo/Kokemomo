#!/usr/bin/env python
# -*- coding:utf-8 -*-

from unittest import TestCase
from nose.tools import ok_, eq_
from kokemomo.plugins.engine.controller.km_wsgi import WSGI_Bottle
from kokemomo.plugins.engine.controller.km_plugin import create_base_plugin


__author__ = 'hiroki'

"""
Test class plugin.

"""

class PluginTestCase(TestCase):

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_create_base_plugin(self):
        result = create_base_plugin()
        ok_(isinstance(result, WSGI_Bottle))
