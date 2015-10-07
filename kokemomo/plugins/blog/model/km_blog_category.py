#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.model.km_storage.impl.km_rdb_adapter import adapter

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

    def __repr__(self):
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)

    @classmethod
    def create(cls, id):
        if id == 'None':
            category = KMBlogCategory()
            category.name = ""
        else:
            category = KMBlogCategory.get(id=id)
        return category
