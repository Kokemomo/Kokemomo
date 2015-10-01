#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'hiroki-m'

import os

from kokemomo.plugins.engine.controller.km_plugin_manager import KMBaseController
from kokemomo.plugins.engine.controller.km_exception import log as log_error
from kokemomo.plugins.engine.controller.km_login import logout, login_auth
from kokemomo.plugins.engine.controller.km_session_manager import get_value_to_session
from kokemomo.plugins.engine.utils.km_utils import get_menu_list
from kokemomo.plugins.engine.controller.km_engine import KMEngine
from kokemomo.settings.common import CHARACTER_SET
from kokemomo.plugins.blog.model.km_blog_info import KMBlogInfo
from kokemomo.plugins.blog.model.km_blog_category import KMBlogCategory
from kokemomo.plugins.blog.model.km_blog_article import KMBlogArticle
from kokemomo.plugins.blog.model.km_blog_comment import KMBlogComment
from kokemomo.plugins.admin import KMAdmin
from kokemomo.plugins.engine.controller.km_storage.impl.km_rdb_adapter import adapter, Transaction, rollback




'''
ブログ
├info ブログの情報
├subscription 購読情報
└category カテゴリ
　└article 記事
　└comment コメント

'''

DATA_DIR_PATH = "/kokemomo/data/blog/"


class KMBlog(KMAdmin):


    def get_name(self):
        return 'blog'


    def get_route_list(self):
        list = super(KMBlog, self).get_route_list() # import admin route list
        list = list + super(KMAdmin, self).get_route_list() # import engine route list
        list = list + (
            {'rule': '/blog-js/<filename>', 'method': 'GET', 'target': self.blog_js_static, 'name': 'blog_static_js'},
            {'rule': '/blog-js/tinymce/<filename>', 'method': 'GET', 'target': self.blog_js_tiny_static, 'name': 'blog_static_tiny_js'},
            {'rule': '/blog-js/tinymce/<child>/<filename>', 'method': 'GET', 'target': self.blog_js_tiny_child_static, 'name': 'blog_static_tiny_js_child'},
            {'rule': '/blog-js/tinymce/<child>/<grandchild>/<filename>', 'method': 'GET', 'target': self.blog_js_tiny_grandchild_static, 'name': 'blog_static_tiny_js_grandchild'},
            {'rule': '/blog-js/tinymce/<child>/<grandchild>/<great_grandchild>/<filename>', 'method': 'GET', 'target': self.blog_js_tiny_great_grandchild_static, 'name': 'blog_static_tiny_js_great_grandchild'},
            {'rule': '/blog-css/<filename>', 'method': 'GET', 'target': self.blog_css_static, 'name': 'blog_static_css'},
            {'rule': '/admin', 'method': 'GET', 'target': self.blog_admin},
            {'rule': '/admin/create_info', 'method': 'POST', 'target': self.blog_admin_create_info},
            {'rule': '/admin/create_category', 'method': 'POST', 'target': self.blog_admin_create_category},
            {'rule': '/admin/create_article', 'method': 'POST', 'target': self.blog_admin_create_article},

            {'rule': '/<blog_url>', 'method': 'GET', 'target': self.blog_page},
            {'rule': '/template/normal/css/<filename>', 'method': 'GET', 'target': self.blog_entry_css_static, 'name':'blog_static_normal_css'},
            {'rule': '/template/normal/js/<filename>', 'method': 'GET', 'target': self.blog_entry_js_static, 'name':'blog_static_normal_js'},
            {'rule': '/<blog_url>/add_comment', 'method': 'POST', 'target': self.blog_add_comment},
        )
        return list


    @log_error
    def blog_js_static(self, filename):
        """
        set javascript files.
        :param filename: javascript file name.
        :return: static path.
        """
        return self.load_static_file(filename, root='kokemomo/plugins/blog/view/resource/js')


    @log_error
    def blog_js_tiny_static(self, filename):
        """
        set javascript files.
        :param filename: javascript file name.
        :return: static path.
        """
        return self.load_static_file(filename, root='kokemomo/plugins/blog/view/resource/js/tinymce')


    @log_error
    def blog_js_tiny_child_static(self, child, filename):
        """
        set javascript files.
        :param filename: javascript file name.
        :return: static path.
        """
        return self.load_static_file(filename, root='kokemomo/plugins/blog/view/resource/js/tinymce/' + child)


    @log_error
    def blog_js_tiny_grandchild_static(self, child, grandchild, filename):
        """
        set javascript files.
        :param filename: javascript file name.
        :return: static path.
        """
        return self.load_static_file(filename, root='kokemomo/plugins/blog/view/resource/js/tinymce/' + child + '/' + grandchild)


    @log_error
    def blog_js_tiny_great_grandchild_static(self, child, grandchild, great_grandchild, filename):
        """
        set javascript files.
        :param filename: javascript file name.
        :return: static path.
        """
        return self.load_static_file(filename, root='kokemomo/plugins/blog/view/resource/js/tinymce/' + child + '/' + grandchild + '/' + great_grandchild)


    @log_error
    def blog_css_static(self, filename):
        """
        set css files.
        :param filename: css file name.
        :return: static path.
        """
        return self.load_static_file(filename, root='kokemomo/plugins/blog/view/resource/css')


    @log_error
    def blog_admin(self):
        '''
        blog admin page
        :return: template
        '''
        type = self.data.get_request_parameter('type', default='dashboard')
        id = self.data.get_request_parameter('id', default='None')
        if self.data.get_request_parameter('delete', default=False):
            self.delete(type, id)
        values = {}
        # branched by type
        if type == 'dashboard':
            values['info'] = KMBlogInfo.all()
        elif type == 'info':
            values['info'] = KMBlogInfo.create(id)
        elif type == 'category_list':
            values['info'] = KMBlogInfo.all()
            values['category'] = KMBlogCategory.all()
        elif type == 'category':
            values['info'] = KMBlogInfo.all()
            values['category'] = KMBlogCategory.create(id)
        elif type == 'article_list':
            values['info'] = KMBlogInfo.all()
            for info in values['info']:
                info.articles = KMBlogArticle.find(info_id=info.id)
        elif type == 'article':
            info_id = self.data.get_request_parameter('info_id')
            values['info'] = KMBlogInfo.get(id=info_id)
            values['category'] = KMBlogCategory.find(info_id=info_id)
            values['article'] = KMBlogArticle.create(id)
        return self.get_template(type, values)


    def delete(self, type, id):
        if type == 'dashboard':
            KMBlogInfo.delete(id)
            KMBlogCategory.delete(info_id=id)
            KMBlogArticle.delete(info_id=id)
        elif type == 'category_list':
            KMBlogCategory.delete(id=id)
            KMBlogArticle.delete(category_id=id)
        elif type == 'article_list':
            KMBlogArticle.delete(id)


    def get_template(self, type, values):
        user_id = get_value_to_session(self.data.get_request(), 'user_id')
        menu_list = get_menu_list()
        return self.render('kokemomo/plugins/blog/view/admin', url=self.get_url, user_id=user_id, menu_list=menu_list, type=type,
                        values=values)


    @log_error
    def blog_admin_create_info(self):
        '''
        Create Blog Information.
        :return:
        '''
        values = self.create_info_values(self.data.get_request())
        if len(values['errors']) == 0:
            info = values['info']
            with Transaction.begin():
                Transaction.add(info)
            Transaction.commit()
            type = 'result'
        else:
            type = 'info'
        return self.get_template(type, values)


    def create_info_values(self,request):

        '''
        Create Blog Information Values.
        :param request:
        :return:
        '''
        values = {}
        errors = {}
        id = request.params.get('id', default='None')
        values['message'] = 'ブログを新規作成しました。' if id == 'None' else 'ブログを更新しました。'
        info = KMBlogInfo.create(id)
        info.name = request.forms.get('name', default='').decode(CHARACTER_SET)
        if info.name == '':
            errors['name'] = 'ブログ名は必須です。'
        info.url = request.forms.get('url', default='')
        if info.url == '':
            errors['url'] = 'URLは必須です。'
        info.description = request.forms.get('description', default='').decode(CHARACTER_SET)
        values['info'] = info
        values['errors'] = errors
        return values


    @log_error
    def blog_admin_create_category(self):
        '''
        Create Blog Category.
        :return:
        '''
        values = self.create_category_values(self.data.get_request())
        if len(values['errors']) == 0:
            category = values['category']
            with Transaction.begin():
                Transaction.add(category)
            Transaction.commit()
            type = 'result'
        else:
            type = 'category'
            values['category'] = KMBlogCategory.all()
        return self.get_template(type, values)


    def create_category_values(self, request):
        '''
        Create Blog Information Values.
        :param request:
        :return:
        '''
        values = {}
        errors = {}
        id = request.params.get('id', default='None')
        values['message'] = 'カテゴリを新規作成しました。' if id == 'None' else 'カテゴリを更新しました。'
        category = KMBlogCategory.create(id)
        category.name = request.forms.get('name', default='').decode(CHARACTER_SET)
        category.info_id = request.forms.get('info', default='None')
        if category.name == '':
            errors['name'] = 'カテゴリ名は必須です。'
        values['category'] = category
        values['errors'] = errors
        return values


    @log_error
    def blog_admin_create_article(self):
        '''
        Create Blog Article.
        :return:
        '''
        values = self.create_article_values(self.data.get_request())
        if len(values['errors']) == 0:
            article = values['article']
            with Transaction.begin():
                Transaction.add(article)
            Transaction.commit()
            type = 'result'
        else:
            type = 'article'
            values['category'] = KMBlogCategory.all()
        return self.get_template(type, values)


    def create_article_values(self, request):
        '''
        Create Blog Information Values.
        :param request:
        :return:
        '''
        values = {}
        errors = {}
        id = request.params.get('id', default='None')
        article = KMBlogArticle.create(id)
        values['message'] = '記事を新規作成しました。' if id == 'None' else '記事を更新しました。'
        article.info_id = request.forms.get('info_id')
        article.category_id = request.forms.get('category')
        article.title = request.forms.get('title', default='').decode(CHARACTER_SET)
        if article.title == '':
            errors['title'] = '記事名は必須です。'
        article.article = request.forms.get('article', default='').decode(CHARACTER_SET)
        if article.article == '':
            errors['article'] = '記事は必須です。'
        values['article'] = article
        values['errors'] = errors
        return values


    '''
    Templates

    '''


    @log_error
    def blog_page(self, blog_url):
        info = KMBlogInfo.find(url=blog_url)[0]
        info.articles = KMBlogArticle.find(info_id=info.id)
        for article in info.articles:
            article.comments = KMBlogComment.find(article_id=article.id)
        values = {'info': info}
        return self.render('kokemomo/plugins/blog/view/template/normal/normal', url=self.get_url, values=values, blog_url=blog_url)


    @log_error
    def blog_entry_css_static(self, filename):
        return self.load_static_file(filename, root='kokemomo/plugins/blog/view/template/normal/css/')


    @log_error
    def blog_entry_js_static(self, filename):
        return self.load_static_file(filename, root='kokemomo/plugins/blog/view/template/normal/js/')


    @log_error
    def blog_add_comment(self, blog_url):
        blog_comment = KMBlogComment()
        article_id = self.data.get_request_parameter('id', default='None')
        comment = self.data.get_request_parameter('comment', default='').decode(CHARACTER_SET)
        blog_comment.article_id = article_id
        blog_comment.comment = comment
        blog_comment.save()
        self.redirect('/blog/' + blog_url)

    # def create_blog_file(info):
    #    path = os.path.abspath(os.curdir) + DATA_DIR_PATH + info.url
    #    if not os.path.exists(path):
    #        os.makedirs(path)

