#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.model.km_storage.impl.km_rdb_adapter import adapter
from kokemomo.plugins.engine.model.km_validate_error import KMValidateError


__author__ = 'hiroki'

"""
It is blog category table to be used in the KOKEMOMO.
[Table Layouts]
    id:Integer
    info_id:Integer
    name:Text
    create_at:DateTime(Automatic Updates)
    update_at:DateTime(Automatic Updates)

"""


class KMBlogCategory(adapter.Model):
    __tablename__ = 'km_blog_category'
    id = adapter.Column(adapter.Integer, autoincrement=True, primary_key=True)
    info_id = adapter.Column(adapter.Integer)
    name = adapter.Column(adapter.Text)

    def __init__(self, data=None):
        if data is None:
            self.name = ''
        else:
            self.set_data(data)

    def __repr__(self):
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)


    def set_data(self, data):
        self.error = None
        self.name = data.get_request_parameter('name', default='', decode=True)
        self.info_id = data.get_request_parameter('info_id', default=None)


    def validate(self):
        self.error = KMValidateError()
        if self.name == '':
            self.error.add_data(id='name', message='ブログ名は必須です。')
        if self.error.size() == 0:
            return True
        else:
            return False

    @classmethod
    def get(self, id):
        if id is None:
            info = KMBlogCategory()
        else:
            info = super(KMBlogCategory, self).get(id=id)
        return info