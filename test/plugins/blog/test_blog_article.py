#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'hiroki-m'
import bcrypt
from unittest import TestCase
from mox import Mox, ExpectedMethodCallsError, IsA
from nose.tools import ok_, eq_, raises, with_setup
from kokemomo.plugins.blog.model.km_blog_article import KMBlogArticle
from kokemomo.plugins.engine.controller.km_data import KMData
from kokemomo.plugins.engine.model.km_storage import initialize

class BlogArticleTest(TestCase):

    test_info_id = 'test_info_id'
    test_category_id = 'test_category_id'
    test_title = 'test_title'
    test_article = 'test_article'

    def setUp(self):
        initialize(rdb_path='sqlite:///:memory:')
        self.mocker = Mox()
        model = KMBlogArticle()
        model.save() # id = 1のデータを登録


    def tearDown(self):
        pass


    def test_set_data(self):
        data = self.mocker.CreateMock(KMData)
        data.get_request_parameter('info_id').AndReturn(self.test_info_id)
        data.get_request_parameter('category_id').AndReturn(self.test_category_id)
        data.get_request_parameter('title', default='', decode=True).AndReturn(self.test_title)
        data.get_request_parameter('article', default='', decode=True).AndReturn(self.test_article)
        self.mocker.ReplayAll()
        model = KMBlogArticle()
        model.set_data(data);
        # KMDataで指定した値が設定されること
        eq_(model.info_id, self.test_info_id)
        eq_(model.category_id, self.test_category_id)
        eq_(model.title, self.test_title)
        eq_(model.error, None)
        self.mocker.UnsetStubs()
        self.mocker.VerifyAll()


    def test_validate(self):
        model = KMBlogArticle()
        # 各フィールドに値が設定されていない場合はFalseが返され、エラーが取得できること
        eq_(model.validate(), False)
        eq_(model.error.get('title')['message'], '記事名は必須です。')
        # 各フィールドに値が設定されている場合はTrueが返されること
        model = KMBlogArticle()
        model.title = self.test_title
        eq_(model.validate(), True)


    def test_get(self):
        model = KMBlogArticle.get(None)
        # id = Noneの場合は新規モデルが取得できること
        eq_(model.id, None)
        model = KMBlogArticle.get(1)
        # id = 1の場合は登録済みのモデルが取得できること
        eq_(model.id, 1)


    def test_save_data_error(self):
        data = self.mocker.CreateMock(KMData)
        data.get_request_parameter('info_id').AndReturn('')
        data.get_request_parameter('category_id').AndReturn('')
        data.get_request_parameter('title', default='', decode=True).AndReturn('')
        data.get_request_parameter('article', default='', decode=True).AndReturn('')
        self.mocker.ReplayAll()
        model = KMBlogArticle.save_data(None, data)
        # フィールドに値が設定されていない場合はエラーが返ること
        eq_(model.error.size(), 1)
        self.mocker.VerifyAll()


    def test_save_data_id_none(self):
        data = self.mocker.CreateMock(KMData)
        data.get_request_parameter('info_id').AndReturn(self.test_info_id)
        data.get_request_parameter('category_id').AndReturn(self.test_category_id)
        data.get_request_parameter('title', default='', decode=True).AndReturn(self.test_title)
        data.get_request_parameter('article', default='', decode=True).AndReturn(self.test_article)
        self.mocker.ReplayAll()
        model = KMBlogArticle.save_data(None, data)
        # idが指定されていない場合は新規で登録されること(id=2)
        eq_(model.error.size(), 0)
        eq_(model.id, 2)
        eq_(model.info_id, self.test_info_id)
        eq_(model.category_id, self.test_category_id)
        eq_(model.title, self.test_title)
        eq_(model.article, self.test_article)
        self.mocker.VerifyAll()


    def test_save_data(self):

        model = KMBlogArticle.get(1)
        eq_(model.id, 1)
        eq_(model.info_id, None)
        eq_(model.category_id, None)
        eq_(model.title, '')
        eq_(model.article, '')
        data = self.mocker.CreateMock(KMData)
        data.get_request_parameter('info_id').AndReturn(self.test_info_id)
        data.get_request_parameter('category_id').AndReturn(self.test_category_id)
        data.get_request_parameter('title', default='', decode=True).AndReturn(self.test_title)
        data.get_request_parameter('article', default='', decode=True).AndReturn(self.test_article)
        self.mocker.ReplayAll()
        model = KMBlogArticle.save_data(1, data)
        # 既存データのidが指定された場合は値が上書きされること
        eq_(model.error.size(), 0)
        eq_(model.id, 1)
        eq_(model.info_id, self.test_info_id)
        eq_(model.category_id, self.test_category_id)
        eq_(model.title, self.test_title)
        eq_(model.article, self.test_article)
        self.mocker.VerifyAll()
