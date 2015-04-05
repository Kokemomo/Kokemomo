#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'hiroki-m'

import os

from kokemomo.lib.bottle import template, route, static_file, url, request, response, redirect
from kokemomo.plugins.engine.controller.km_db_manager import *
from kokemomo.plugins.engine.controller.km_session_manager import get_value_to_session
from kokemomo.plugins.engine.utils.km_utils import get_menu_list
from kokemomo.plugins.blog.model.km_blog_info import KMBlogInfo, create as create_info, find_all as find_info_list, update as save_info, find_by_url as find_info_by_url, find as find_info
from kokemomo.plugins.blog.model.km_blog_category import KMBlogCategory, create as create_category, find_all as find_category_list, update as save_category
from kokemomo.plugins.blog.model.km_blog_article import KMBlogArticle, create as create_article, find_all as find_article_list, update as save_article, find_by_info_id as find_article_list_by_info_id

'''
ブログ
├info ブログの情報
├subscription 購読情報
└category カテゴリ
　└article 記事
　└comment コメント

'''

DATA_DIR_PATH = "/kokemomo/data/blog/"

db_manager = KMDBManager("engine")

@route('/blog/js/<filename>', name='blog_static_js')
def blog_js_static(filename):
    """
    set javascript files.
    :param filename: javascript file name.
    :return: static path.
    """
    return static_file(filename, root='kokemomo/plugins/blog/view/resource/js')


@route('/blog/css/<filename>', name='blog_static_css')
def blog_entry_css_static(filename):
    """
    set css files.
    :param filename: css file name.
    :return: static path.
    """
    return static_file(filename, root='kokemomo/plugins/blog/view/resource/css')


@route('/blog/admin')
def blog_admin():
    '''
    blog admin page
    :return: template
    '''
    try:
        session = db_manager.get_session()
        type = request.params.get('type', default='dashboard')
        id = request.params.get('id', default='None')
        values = {}
        # branched by type
        if type == 'dashboard':
            values['info'] = find_info_list(session)
        elif type == 'info':
            values['info'] = create_info(id, session);
        elif type == 'category_list':
            values['category'] = find_category_list(session);
        elif type == 'category':
            values['category'] = create_category(id, session);
        elif type == 'article_list':
            values['info'] = find_info_list(session)
            for info in values['info']:
                info.articles = find_article_list_by_info_id(info.id, session)
        elif type == 'article':
            info_id = request.params.get('info_id')
            values['info'] = find_info(info_id, session)
            values['category'] = find_category_list(session)
            values['article'] = create_article(id, session)
        return get_template(type, values)
    finally:
        session.close()

def get_template(type, values):
    user_id = get_value_to_session(request, 'user_id')
    menu_list = get_menu_list()
    return template('kokemomo/plugins/blog/view/admin', url=url, user_id=user_id, menu_list=menu_list, type=type, values=values)


@route('/blog/admin/create_info', method='POST')
def blog_admin_create_info():
    '''
    Create Blog Information.
    :return:
    '''
    try:
        session = db_manager.get_session()
        values = create_info_values(request, session)
        if len(values['errors']) == 0:
            save_info(values['info'], session)
            type='result'
        else:
            type='info'
        return get_template(type, values)
    finally:
        session.close()


def create_info_values(request, session):
    '''
    Create Blog Information Values.
    :param request:
    :return:
    '''
    values = {}
    errors = {}
    id = request.params.get('id', default='None')
    values['message'] = 'ブログを新規作成しました。' if id == 'None' else 'ブログを更新しました。'
    info = create_info(id, session)
    info.name = request.forms.get('name', default='')
    if info.name == '':
        errors['name'] = 'ブログ名は必須です。'
    info.url = request.forms.get('url', default='')
    if info.url == '':
        errors['url'] = 'URLは必須です。'
    info.description = request.forms.get('description', default='')
    values['info'] = info
    values['errors'] = errors
    return values


@route('/blog/admin/create_category', method='POST')
def blog_admin_create_category():
    '''
    Create Blog Category.
    :return:
    '''
    try:
        session = db_manager.get_session()
        values = create_category_values(request, session)
        if len(values['errors']) == 0:
            save_category(values['category'], session)
            type='result'
        else:
            type='category'
        return get_template(type, values)
    finally:
        session.close()

def create_category_values(request, session):
    '''
    Create Blog Information Values.
    :param request:
    :return:
    '''
    values = {}
    errors = {}
    id = request.params.get('id', default='None')
    values['message'] = 'カテゴリを新規作成しました。' if id == 'None' else 'カテゴリを更新しました。'
    category = create_category(id, session)
    category.name = request.forms.get('name', default='')
    if category.name == '':
        errors['name'] = 'カテゴリ名は必須です。'
    values['category'] = category
    values['errors'] = errors
    return values

@route('/blog/admin/create_article', method='POST')
def blog_admin_create_article():
    '''
    Create Blog Article.
    :return:
    '''
    try:
        session = db_manager.get_session()
        values = create_article_values(request, session)
        if len(values['errors']) == 0:
            save_article(values['article'], session)
            type='result'
        else:
            type='article'
            values['category'] = find_category_list(session)
        return get_template(type, values)
    finally:
        session.close()

def create_article_values(request, session):
    '''
    Create Blog Information Values.
    :param request:
    :return:
    '''
    values = {}
    errors = {}
    id = request.params.get('id', default='None')
    article = create_article(id, session)
    values['message'] = '記事を新規作成しました。' if id == 'None' else '記事を更新しました。'
    article.info_id = request.forms.get('info_id')
    article.title = request.forms.get('title', default='')
    if article.title == '':
        errors['title'] = '記事名は必須です。'
    article.article = request.forms.get('article', default='')
    if article.article == '':
        errors['article'] = '記事は必須です。'
    values['article'] = article
    values['errors'] = errors
    return values


'''
Templates

'''

@route('/blog/<blog_url>')
def blog_page(blog_url):
    try:
        session = db_manager.get_session()
        info = find_info_by_url(blog_url, session)
        info.articles = find_article_list_by_info_id(info.id, session)
        values = {'info':info}
        return template('kokemomo/plugins/blog/view/template/normal/normal', url=url, values=values, blog_url=blog_url)
    finally:
        session.close()

@route('/blog/template/normal/css/<filename>', name='blog_static_normal_css')
def blog_entry_css_static(filename):
    return static_file(filename, root='kokemomo/plugins/blog/view/template/normal/css/')

@route('/blog/template/normal/js/<filename>', name='blog_static_normal_js')
def blog_entry_css_static(filename):
    return static_file(filename, root='kokemomo/plugins/blog/view/template/normal/js/')

#def create_blog_file(info):
#    path = os.path.abspath(os.curdir) + DATA_DIR_PATH + info.url
#    if not os.path.exists(path):
#        os.makedirs(path)
