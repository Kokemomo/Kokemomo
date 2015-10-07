#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.model.km_storage.impl.km_rdb_adapter import adapter
from kokemomo.plugins.engine.model.km_validate_error import KMValidateError

__author__ = 'hiroki'

"""
It is blog information table to be used in the Kokemomo.
[Table Layouts]
    id:Integer
    name:Text
    url:Text
    description:Text
    create_at:DateTime(Automatic Updates)
    update_at:DateTime(Automatic Updates)
"""


class KMBlogInfo(adapter.Model):
    __tablename__ = 'km_blog_info'
    id = adapter.Column(adapter.Integer, autoincrement=True, primary_key=True)
    name = adapter.Column(adapter.Text)
    url = adapter.Column(adapter.Text)
    description = adapter.Column(adapter.Text)

    def __init__(self, data=None):
        if data is None:
            self.name = ''
            self.url = ''
            self.description = ''
        else:
            self.set_data(data)

    def __repr__(self):
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)


    def set_data(self, data):
        self.error = None
        self.name = data.get_request_parameter('name', default='', decode=True)
        self.url = data.get_request_parameter('url', default='')
        self.description = data.get_request_parameter('description', default='', decode=True)

    def validate(self):
        self.error = KMValidateError()
        if self.name == '':
            self.error.add_data(id='name', message='ブログ名は必須です。')
        if self.url == '':
            self.error.add_data(id='url', message='URLは必須です。')
        if self.error.size() == 0:
            return True
        else:
            return False
