#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.model.km_storage.impl.km_rdb_adapter import adapter

__author__ = 'hiroki'

"""
It is blog subscription table to be used in the KOKEMOMO.
[Table Layouts]
    id:Integer
    user_id:Integer
    target_id:Integer
    create_at:DateTime(Automatic Updates)
    update_at:DateTime(Automatic Updates)

"""


class KMBlogSubscription(adapter.Model):
    __tablename__ = 'km_blog_subscription'
    id = adapter.Column(adapter.Integer, autoincrement=True, primary_key=True)
    user_id = adapter.Column(adapter.Integer)
    target_id = adapter.Column(adapter.Integer)

    def __repr__(self):
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)
