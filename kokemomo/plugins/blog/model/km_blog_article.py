#!/usr/bin/env python
# -*- coding:utf-8 -*-

from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.model.km_storage.impl.km_rdb_adapter import adapter
from kokemomo.plugins.engine.model.km_validate_error import KMValidateError


__author__ = 'hiroki'

"""
It is blog article table to be used in the KOKEMOMO.
[Table Layouts]
    id:Integer
    category_id:Integer
    title:Text
    article:Text
    post_date:DateTime
    create_at:DateTime(Automatic Updates)
    update_at:DateTime(Automatic Updates)

"""


class KMBlogArticle(adapter.Model):
    __tablename__ = 'km_blog_article'
    id = adapter.Column(adapter.Integer, autoincrement=True, primary_key=True)
    info_id = adapter.Column(adapter.Integer)
    category_id = adapter.Column(adapter.Integer)
    title = adapter.Column(adapter.Text)
    caption = adapter.Column(adapter.Text)
    article = adapter.Column(adapter.Text)
    tag = adapter.Column(adapter.Text)
    post_date = adapter.Column(adapter.DateTime)

    def __init__(self, data=None):
        if data is None:
            self.title = ''
            self.caption = ''
            self.article = ''
            self.tag = ''
            self.post_date = datetime.datetime.now()
        else:
            self.set_data(data)

    def __repr__(self):
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)


    def set_data(self, data):
        self.error = None
        self.info_id = data.get_request_parameter('info_id')
        self.category_id = data.get_request_parameter('category_id')
        self.title = data.get_request_parameter('title', default='')
        self.caption = data.get_request_parameter('caption', default='')
        self.article = data.get_request_parameter('article', default='')
        self.tag = data.get_request_parameter('tag', default='')
        self.post_date = datetime.datetime.now()


    def validate(self):
        self.error = KMValidateError()
        if self.title == '':
            self.error.add_data(id='title', message='記事名は必須です。')
        if self.caption == '':
            self.error.add_data(id='caption', message='見出しは必須です。')
        if self.error.size() == 0:
            return True
        else:
            return False

    @classmethod
    def get(self, id):
        if id is None:
            info = KMBlogArticle()
        else:
            info = super(KMBlogArticle, self).get(id=id)
        return info

    @classmethod
    def save_data(self, id, data):
        if id is None:
            article = KMBlogArticle(data)
        else:
            article = KMBlogArticle.get(id=id)
            article.set_data(data)
        if article.validate():
            article.save()
        return article