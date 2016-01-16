#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'hiroki-m'
import bcrypt
from unittest import TestCase
from mox import Mox, ExpectedMethodCallsError, IsA
from nose.tools import ok_, eq_, raises, with_setup
from kokemomo.plugins.blog.controller.km_blog import KMBlog
from kokemomo.plugins.blog.model.km_blog_info import KMBlogInfo
from kokemomo.plugins.blog.model.km_blog_article import KMBlogArticle
from kokemomo.plugins.blog.model.km_blog_category import KMBlogCategory
from kokemomo.plugins.engine.controller.km_data import KMData
from kokemomo.plugins.engine.model.km_storage import initialize

class BlogTest(TestCase):

    def setUp(self):
        initialize(rdb_path='sqlite:///:memory:')
        self.mocker = Mox()
        info = KMBlogInfo()
        info.save()

        category = KMBlogCategory()
        category.save()

        category2 = KMBlogCategory()
        category2.info_id = info.id
        category2.save()

        article = KMBlogArticle()
        article.info_id = info.id
        article.save()

        self.values = {'info': [info]}

        self.values2 = {'info': KMBlogInfo()}

        self.values3 = {'info': info}

        self.values4 = {'info': [info], 'category': [category, category2]}

        self.values5 = {'info': [info], 'category': KMBlogCategory()}

        self.values6 = {'info': [info], 'category': category}

        self.values7 = {'info': [info], 'article': [article]}

        self.values8 = {'info': info, 'category': [category2], 'article':article}

    def tearDown(self):
        pass


    def test_blog_dashbord(self):
        # typeが'dashboard'の場合
        blog = KMBlog()
        data = self.mocker.CreateMock(KMData)
        data.get_request_parameter('type', default='dashboard').AndReturn('dashboard')
        data.get_request_parameter('id', default=None).AndReturn(None)
        data.get_request_parameter('delete', default=False).AndReturn(False)
        data.get_user_id().AndReturn('hoge')
        # get_template用にもう一つモックを作成
        data2 = self.mocker.CreateMock(KMData)
        data2.get_user_id().AndReturn('hoge')

        self.mocker.ReplayAll()
        blog.data = data
        target = blog.blog_admin()
        blog.data = data2
        actual = blog.get_template('dashboard', self.values)
        eq_(target, actual) # 同じhtmlが生成されていることを確認
        self.mocker.UnsetStubs()
        self.mocker.VerifyAll()


    def test_blog_info_id_none(self):
        # typeが'info'の場合
        blog = KMBlog()
        data = self.mocker.CreateMock(KMData)
        data.get_request_parameter('type', default='dashboard').AndReturn('info')
        data.get_request_parameter('id', default=None).AndReturn(None) # id is None.
        data.get_request_parameter('delete', default=False).AndReturn(False)
        data.get_user_id().AndReturn('hoge')
        data2 = self.mocker.CreateMock(KMData)
        data2.get_user_id().AndReturn('hoge')

        self.mocker.ReplayAll()
        blog.data = data
        target = blog.blog_admin()
        blog.data = data2
        actual = blog.get_template('info', self.values2)
        eq_(target, actual)
        self.mocker.UnsetStubs()
        self.mocker.VerifyAll()


    def test_blog_info_id_not_none(self):
        # typeが'info'の場合
        blog = KMBlog()
        data = self.mocker.CreateMock(KMData)
        data.get_request_parameter('type', default='dashboard').AndReturn('info')
        data.get_request_parameter('id', default=None).AndReturn(self.values['info'][0].id)# id is not None.
        data.get_request_parameter('delete', default=False).AndReturn(False)
        data.get_user_id().AndReturn('hoge')
        data2 = self.mocker.CreateMock(KMData)
        data2.get_user_id().AndReturn('hoge')

        self.mocker.ReplayAll()
        blog.data = data
        target = blog.blog_admin()
        blog.data = data2
        actual = blog.get_template('info', self.values3)
        eq_(target, actual)
        self.mocker.UnsetStubs()
        self.mocker.VerifyAll()


    def test_blog_category_list(self):
        # typeが'category_list'の場合
        blog = KMBlog()
        data = self.mocker.CreateMock(KMData)
        data.get_request_parameter('type', default='dashboard').AndReturn('category_list')
        data.get_request_parameter('id', default=None).AndReturn(None)
        data.get_request_parameter('delete', default=False).AndReturn(False)
        data.get_user_id().AndReturn('hoge')
        data2 = self.mocker.CreateMock(KMData)
        data2.get_user_id().AndReturn('hoge')

        self.mocker.ReplayAll()
        blog.data = data
        target = blog.blog_admin()
        blog.data = data2
        actual = blog.get_template('category_list', self.values4)
        eq_(target, actual)
        self.mocker.UnsetStubs()
        self.mocker.VerifyAll()


    def test_blog_category_id_none(self):
        # typeが'category'の場合
        blog = KMBlog()
        data = self.mocker.CreateMock(KMData)
        data.get_request_parameter('type', default='dashboard').AndReturn('category')
        data.get_request_parameter('id', default=None).AndReturn(None)
        data.get_request_parameter('delete', default=False).AndReturn(False)
        data.get_user_id().AndReturn('hoge')
        data2 = self.mocker.CreateMock(KMData)
        data2.get_user_id().AndReturn('hoge')

        self.mocker.ReplayAll()
        blog.data = data
        target = blog.blog_admin()
        blog.data = data2
        actual = blog.get_template('category', self.values5)
        eq_(target, actual)
        self.mocker.UnsetStubs()
        self.mocker.VerifyAll()


    def test_blog_category_id_not_none(self):
        # typeが'category'の場合
        blog = KMBlog()
        data = self.mocker.CreateMock(KMData)
        data.get_request_parameter('type', default='dashboard').AndReturn('category')
        data.get_request_parameter('id', default=None).AndReturn(self.values6['category'].id)
        data.get_request_parameter('delete', default=False).AndReturn(False)
        data.get_user_id().AndReturn('hoge')
        data2 = self.mocker.CreateMock(KMData)
        data2.get_user_id().AndReturn('hoge')

        self.mocker.ReplayAll()
        blog.data = data
        target = blog.blog_admin()
        blog.data = data2
        actual = blog.get_template('category', self.values6)
        eq_(target, actual)
        self.mocker.UnsetStubs()
        self.mocker.VerifyAll()


    def test_blog_article_list(self):
        # typeが'category'の場合
        blog = KMBlog()
        data = self.mocker.CreateMock(KMData)
        data.get_request_parameter('type', default='dashboard').AndReturn('article_list')
        data.get_request_parameter('id', default=None).AndReturn(None)
        data.get_request_parameter('delete', default=False).AndReturn(False)
        data.get_user_id().AndReturn('hoge')
        data2 = self.mocker.CreateMock(KMData)
        data2.get_user_id().AndReturn('hoge')

        self.mocker.ReplayAll()
        blog.data = data
        target = blog.blog_admin()
        blog.data = data2
        actual = blog.get_template('article_list', self.values7)
        eq_(target, actual)
        self.mocker.UnsetStubs()
        self.mocker.VerifyAll()


    def test_blog_article_id_none(self):
        # typeが'category'の場合
        blog = KMBlog()
        data = self.mocker.CreateMock(KMData)
        data.get_request_parameter('type', default='dashboard').AndReturn('article')
        data.get_request_parameter('id', default=None).AndReturn(self.values8['article'].id)
        data.get_request_parameter('delete', default=False).AndReturn(False)
        data.get_request_parameter('info_id').AndReturn(self.values8['info'].id)
        data.get_user_id().AndReturn('hoge')
        data2 = self.mocker.CreateMock(KMData)
        data2.get_user_id().AndReturn('hoge')

        self.mocker.ReplayAll()
        blog.data = data
        target = blog.blog_admin()
        blog.data = data2
        actual = blog.get_template('article', self.values8)
        eq_(target, actual)
        self.mocker.UnsetStubs()
        self.mocker.VerifyAll()


    def test_delete_type_dashboard(self):
        id = self.values3['info'].id
        info = KMBlogInfo.get(id)
        category = KMBlogCategory.find(info_id=id)
        article = KMBlogArticle.find(info_id=id)
        eq_(info is not None, True)
        eq_(len(category), 1)
        eq_(len(article), 1)
        blog = KMBlog()
        blog.delete('dashboard', id)
        info = KMBlogInfo.get(id)
        category = KMBlogCategory.find(info_id=id)
        article = KMBlogArticle.find(info_id=id)
        eq_(info is None, True)
        eq_(len(category), 0)
        eq_(len(article), 0)



    def test_delete_type_category_list(self):
        id = self.values3['info'].id
        pass


    def test_delete_type_article_list(self):
        id = self.values3['info'].id
        pass

class TestRequest():

    def __init__(self):
        self.result = ''

    def get_request(self):
        return self

