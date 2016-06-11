#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'hiroki-m'
import bcrypt
from unittest import TestCase
from mox import Mox, ExpectedMethodCallsError, IsA
from nose.tools import ok_, eq_, raises, with_setup
from kokemomo.plugins.blog.model.km_blog_comment import KMBlogComment
from kokemomo.plugins.engine.controller.km_data import KMData
from kokemomo.plugins.engine.model.km_storage import initialize

class BlogCommentTest(TestCase):

    def setUp(self):
        initialize(rdb_path='sqlite:///:memory:')
        self.mocker = Mox()
        model = KMBlogComment()
        model.save() # id = 1のデータを登録


    def tearDown(self):
        pass


    def test_set_data(self):
        model = KMBlogComment()
        test_article_id = 'test_article_id'
        test_comment = 'test_comment'
        data = self.mocker.CreateMock(KMData)
        data.get_request_parameter('article_id', default='', decode=True).AndReturn(test_article_id)
        data.get_request_parameter('comment', default='', decode=True).AndReturn(test_comment)
        self.mocker.ReplayAll()
        model.set_data(data);
        # KMDataで指定した値が設定されること
        eq_(model.article_id, test_article_id)
        eq_(model.comment, test_comment)
        eq_(model.error, None)
        self.mocker.UnsetStubs()
        self.mocker.VerifyAll()
