#!/usr/bin/env python
# -*- coding:utf-8 -*-

from mox import Mox, ExpectedMethodCallsError
from nose.tools import ok_, eq_, raises, with_setup
from kokemomo.plugins.engine.utils.km_config import (
    get_logging_setting,
    get_logging_setting_by_name,
)
from kokemomo.lib.bottle import Bottle

__author__ = 'hiroki'

"""
km_configのテスト.


"""

class TestConfig:

    @classmethod
    def setup_class(clazz):
        pass

    @classmethod
    def teardown_class(clazz):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_get_logging(self):
        settings = get_logging_setting()
        pass

    def test_get_logging_by_name(self):
        settings = get_logging_setting_by_name('Rotate')
        pass

    def test_get_plugin(self):
        settings = get_logging_setting()
        pass