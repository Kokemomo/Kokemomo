#!/usr/bin/env python
# -*- coding:utf-8 -*-

import test_server
from webtest import TestApp

__author__ = 'hiroki'

"""
Test class security.

"""

class TestSecurity:

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

    def test_set_response_charset(self):
        app = TestApp(test_server.app)
        result = app.get('/get_test?value=test')
        assert result.charset == 'shift_jis'
