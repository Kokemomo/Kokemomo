#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.controller.km_storage.impl.km_rdb_adapter import adapter, Transaction, rollback

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


    def __repr__(self):
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)


    @classmethod
    def create(cls, id):
        if id == 'None':
            info = KMBlogInfo()
            info.name = ""
            info.url = ""
            info.description = ""
        else:
            info = KMBlogInfo.get(id=id)
        return info

