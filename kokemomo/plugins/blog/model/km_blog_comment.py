#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.model.km_storage.impl.km_rdb_adapter import adapter

__author__ = 'hiroki'

"""
It is blog comment table to be used in the KOKEMOMO.
[Table Layouts]
    id:Integer
    article_id:Integer
    comment:Text
    create_at:DateTime(Automatic Updates)
    update_at:DateTime(Automatic Updates)

"""


class KMBlogComment(adapter.Model):
    __tablename__ = 'km_blog_comment'
    id = adapter.Column(adapter.Integer, autoincrement=True, primary_key=True)
    article_id = adapter.Column(adapter.Integer)
    comment = adapter.Column(adapter.Text)

    def __init__(self, data=None):
        if data is None:
            self.comment = ''
        else:
            self.set_data(data)

    def __repr__(self):
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)


    def set_data(self, data):
        self.error = None
        self.article_id = data.get_request_parameter('article_id', default='')
        self.comment = data.get_request_parameter('comment', default='')

    def validate(self):
        return True
