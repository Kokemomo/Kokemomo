#!/usr/bin/env python
# -*- coding:utf-8 -*-

from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.controller.km_storage.impl.km_rdb_adapter import adapter, Transaction, rollback

__author__ = 'hiroki'

"""
It is blog article table to be used in the KOKEMOMO.
[Table Layouts]
    id:Integer
    info_id:Integer
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
    article = adapter.Column(adapter.Text)
    post_date = adapter.Column(adapter.DateTime)

    def __repr__(self):
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)

    @classmethod
    def create(cls, id):
        if id == 'None':
            article = KMBlogArticle()
            article.info_id = 0
            article.category_id = 0
            article.title = ""
            article.article = ""
            article.post_date = datetime.datetime.now()
        else:
            article = KMBlogArticle.get(id)
        return article
