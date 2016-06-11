#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'hiroki-m'
import bcrypt
from unittest import TestCase
from mox import Mox, ExpectedMethodCallsError, IsA
from nose.tools import ok_, eq_, raises, with_setup
from kokemomo.plugins.blog.model.km_blog_info import KMBlogInfo
from kokemomo.plugins.engine.controller.km_data import KMData
from kokemomo.plugins.engine.model.km_storage import initialize

class BlogInfoTest(TestCase):

    test_name = 'test_name'
    test_url = 'test_url'
    test_description = 'test_description'

    def setUp(self):
        initialize(rdb_path='sqlite:///:memory:')
        self.mocker = Mox()
        model = KMBlogInfo()
        model.save() # id = 1のデータを登録


    def tearDown(self):
        pass


    def test_set_data(self):
        model = KMBlogInfo()
        data = self.mocker.CreateMock(KMData)
        data.get_request_parameter('name', default='', decode=True).AndReturn(self.test_name)
        data.get_request_parameter('url', default='').AndReturn(self.test_url)
        data.get_request_parameter('description', default='', decode=True).AndReturn(self.test_description)
        self.mocker.ReplayAll()
        model.set_data(data);
        # KMDataで指定した値が設定されること
        eq_(model.name, self.test_name)
        eq_(model.url, self.test_url)
        eq_(model.description, self.test_description)
        eq_(model.error, None)
        self.mocker.UnsetStubs()
        self.mocker.VerifyAll()


    def test_validate(self):
        model = KMBlogInfo()
        # 各フィールドに値が設定されていない場合はFalseが返され、エラーが取得できること
        eq_(model.validate(), False)
        eq_(model.error.get('name')['message'], 'ブログ名は必須です。')
        eq_(model.error.get('url')['message'], 'URLは必須です。')
        # 各フィールドに値が設定されている場合はTrueが返されること
        model = KMBlogInfo()
        model.name = self.test_name
        model.url = self.test_url
        eq_(model.validate(), True)


    def test_get(self):
        model = KMBlogInfo.get(None)
        # id = Noneの場合は新規モデルが取得できること
        eq_(model.id, None)
        model = KMBlogInfo.get(1)
        # id = 1の場合は登録済みのモデルが取得できること
        eq_(model.id, 1)


    def test_save_data_error(self):
        data = self.mocker.CreateMock(KMData)
        data.get_request_parameter('name', default='', decode=True).AndReturn('')
        data.get_request_parameter('url', default='').AndReturn('')
        data.get_request_parameter('description', default='', decode=True).AndReturn('')
        self.mocker.ReplayAll()
        model = KMBlogInfo.save_data(None, data)
        # フィールドに値が設定されていない場合はエラーが返ること
        eq_(model.error.size(), 2)
        self.mocker.VerifyAll()


    def test_save_data_id_none(self):
        data = self.mocker.CreateMock(KMData)
        data.get_request_parameter('name', default='', decode=True).AndReturn(self.test_name)
        data.get_request_parameter('url', default='').AndReturn(self.test_url)
        data.get_request_parameter('description', default='', decode=True).AndReturn(self.test_description)
        self.mocker.ReplayAll()
        model = KMBlogInfo.save_data(None, data)
        # idが指定されていない場合は新規で登録されること(id=2)
        eq_(model.error.size(), 0)
        eq_(model.id, 2)
        eq_(model.name, self.test_name)
        eq_(model.url, self.test_url)
        eq_(model.description, self.test_description)
        self.mocker.VerifyAll()


    def test_save_data(self):

        model = KMBlogInfo.get(1)
        eq_(model.id, 1)
        eq_(model.name, '')
        eq_(model.url, '')
        eq_(model.description, '')
        data = self.mocker.CreateMock(KMData)
        data.get_request_parameter('name', default='', decode=True).AndReturn(self.test_name)
        data.get_request_parameter('url', default='').AndReturn(self.test_url)
        data.get_request_parameter('description', default='', decode=True).AndReturn(self.test_description)
        self.mocker.ReplayAll()
        model = KMBlogInfo.save_data(1, data)
        # 既存データのidが指定された場合は値が上書きされること
        eq_(model.error.size(), 0)
        eq_(model.id, 1)
        eq_(model.name, self.test_name)
        eq_(model.url, self.test_url)
        eq_(model.description, self.test_description)
        self.mocker.VerifyAll()
