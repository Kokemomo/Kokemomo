#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.controller.km_storage.impl.km_rdb_adapter import adapter, Transaction, rollback

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

    def __repr__(self):
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)
