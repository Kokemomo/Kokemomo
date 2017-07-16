#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'hiroki-m'

from kokemomo.plugins.engine.controller.km_exception import log as log_error
from kokemomo.plugins.engine.controller.km_session_manager import get_value_to_session
from kokemomo.plugins.engine.utils.km_utils import get_menu_list
from kokemomo.plugins.blog.model.km_blog_info import KMBlogInfo
from kokemomo.plugins.blog.model.km_blog_category import KMBlogCategory
from kokemomo.plugins.blog.model.km_blog_article import KMBlogArticle
from kokemomo.plugins.blog.model.km_blog_comment import KMBlogComment
from kokemomo.plugins.admin import KMAdmin


'''
ブログプラグイン

管理画面でブログの操作を行えるようにadminプラグインを継承しています。

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
            {'rule': '/admin/info', 'method': 'GET', 'target': self.blog_admin_info},
            {'rule': '/admin/category_list', 'method': 'GET', 'target': self.blog_admin_category_list},
            {'rule': '/admin/category', 'method': 'GET', 'target': self.blog_admin_category},
            {'rule': '/admin/article_list', 'method': 'GET', 'target': self.blog_admin_article_list},
            {'rule': '/admin/article', 'method': 'GET', 'target': self.blog_admin_article},
            {'rule': '/admin/create_info', 'method': 'POST', 'target': self.blog_admin_create_info},
            {'rule': '/admin/create_category', 'method': 'POST', 'target': self.blog_admin_create_category},
            {'rule': '/admin/create_article', 'method': 'POST', 'target': self.blog_admin_create_article},
            {'rule': '/admin/delete_info', 'method': 'GET', 'target': self.blog_admin_delete_info},
            {'rule': '/admin/delete_category', 'method': 'GET', 'target': self.blog_admin_delete_category},
            {'rule': '/admin/delete_article', 'method': 'GET', 'target': self.blog_admin_delete_article},

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
    @KMAdmin.action('kokemomo/plugins/blog/view/admin')
    def blog_admin(self):
        '''
        blog admin page
        :return: template
        '''
        self.result['info'] = KMBlogInfo.all()
        self.result['type'] = 'dashboard'
        self.result['menu_list'] = get_menu_list()


    @KMAdmin.action('kokemomo/plugins/blog/view/admin')
    def blog_admin_info(self):
        '''
        blog admin page
        :return: template
        '''
        id = self.data.get_request_parameter('id', default=None)
        self.result['info'] = KMBlogInfo.get(id=id)
        self.result['type'] = 'info'
        self.result['menu_list'] = get_menu_list()

    @KMAdmin.action('kokemomo/plugins/blog/view/admin')
    def blog_admin_category_list(self):
        '''
        blog admin page
        :return: template
        '''
        id = self.data.get_request_parameter('id', default=None)
        self.result['info'] = KMBlogInfo.all()
        self.result['category'] = KMBlogCategory.all()
        self.result['type'] = 'category_list'
        self.result['menu_list'] = get_menu_list()

    @KMAdmin.action('kokemomo/plugins/blog/view/admin')
    def blog_admin_category(self):
        '''
        blog admin page
        :return: template
        '''
        id = self.data.get_request_parameter('id', default=None)
        self.result['info'] = KMBlogInfo.all()
        self.result['category'] = KMBlogCategory.get(id=id)
        self.result['type'] = 'category'
        self.result['menu_list'] = get_menu_list()

    @KMAdmin.action('kokemomo/plugins/blog/view/admin')
    def blog_admin_article_list(self):
        '''
        blog admin page
        :return: template
        '''
        id = self.data.get_request_parameter('id', default=None)
        self.result['info'] = KMBlogInfo.all()
        for info in self.result['info']:
            info.articles = KMBlogArticle.find(info_id=info.id)
        self.result['type'] = 'article_list'
        self.result['menu_list'] = get_menu_list()

    @KMAdmin.action('kokemomo/plugins/blog/view/admin')
    def blog_admin_article(self):
        '''
        blog admin page
        :return: template
        '''
        id = self.data.get_request_parameter('id', default=None)
        info_id = self.data.get_request_parameter('info_id')
        self.result['info'] = KMBlogInfo.get(id=info_id)
        self.result['category'] = KMBlogCategory.find(info_id=info_id)
        self.result['article'] = KMBlogArticle.get(id=id)
        self.result['type'] = 'article'
        self.result['menu_list'] = get_menu_list()


    @log_error
    @KMAdmin.action('kokemomo/plugins/blog/view/admin')
    def blog_admin_delete_info(self):
        id = self.data.get_request_parameter('id', default=None)
        KMBlogInfo.delete_by_id(id)
        KMBlogCategory.delete_by_condition(info_id=id)
        KMBlogArticle.delete_by_condition(info_id=id)


    @log_error
    @KMAdmin.action('kokemomo/plugins/blog/view/admin')
    def blog_admin_delete_category(self):
        id = self.data.get_request_parameter('id', default=None)
        KMBlogCategory.delete_by_id(id)
        KMBlogArticle.delete_by_condition(category_id=id)


    @log_error
    @KMAdmin.action('kokemomo/plugins/blog/view/admin')
    def blog_admin_delete_article(self):
        id = self.data.get_request_parameter('id', default=None)
        KMBlogArticle.delete_by_id(id)


    @log_error
    @KMAdmin.action('kokemomo/plugins/blog/view/admin')
    def blog_admin_create_info(self):
        '''
        Create Blog Information.
        :return:
        '''
        id = self.data.get_request_parameter('id', default=None)
        self.result['info'] = KMBlogInfo.save_data(id, self.data);
        self.result['type'] = 'info'
        self.result['menu_list'] = get_menu_list()

    @log_error
    @KMAdmin.action('kokemomo/plugins/blog/view/admin')
    def blog_admin_create_category(self):
        '''
        Create Blog Category.
        :return:
        '''
        id = self.data.get_request_parameter('id', default=None)
        self.result['info'] = KMBlogInfo.all()
        self.result['category'] = KMBlogCategory.save_data(id, self.data)
        self.result['type'] = 'category'
        self.result['menu_list'] = get_menu_list()


    @log_error
    @KMAdmin.action('kokemomo/plugins/blog/view/admin')
    def blog_admin_create_article(self):
        '''
        Create Blog Article.
        :return:
        '''
        values = {}
        id = self.data.get_request_parameter('id', default=None)
        info_id = self.data.get_request_parameter('info_id')
        self.result['info'] = KMBlogInfo.get(info_id);
        self.result['article'] = KMBlogArticle.save_data(id, self.data);
        self.result['type'] = 'article'
        self.result['menu_list'] = get_menu_list()



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
        blog_comment = KMBlogComment(self.data)
        blog_comment.save()
        return self.blog_page(blog_url)

    # def create_blog_file(info):
    #    path = os.path.abspath(os.curdir) + DATA_DIR_PATH + info.url
    #    if not os.path.exists(path):
    #        os.makedirs(path)

