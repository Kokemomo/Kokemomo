#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.model.km_storage.impl.km_rdb_adapter import adapter

__author__ = 'hiroki'

"""
It is the accessor to group table to be used in the KOKEMOMO.
[Table Layouts]
    id:Integer
    name:String
    parent:Integer
    create_at:DateTime(Automatic Updates)
    update_at:DateTime(Automatic Updates)

[Basic Usage]
You can use the each method from the acquisition of the session in getSession ().

-example-----------------------------------------------------------
from lib.kmgrouptable import get_session,add,find,find_all,delete

def search_parameter():
    session = get_session()
    result = find_all(session)
    session.close()
    return result

-------------------------------------------------------------------
"""


class KMGroup(adapter.Model):
    __tablename__ = 'km_group'
    id = adapter.Column(adapter.Integer, autoincrement=True, primary_key=True)
    name = adapter.Column(adapter.String(50))
    parent_id = adapter.Column(adapter.Integer)


    def __init__(self, data=None):
        if data is None:
            self.name = ''
            self.parent_id = -1
        else:
            self.set_data(data)


    def __repr__(self):
        return create_repr_str(self)


    def get_json(self):
        return create_json(self)


    def set_data(self, data):
        self.error = None
        self.name = data.get_request_parameter('name', default='')
        self.parent_id = data.get_request_parameter('parent_id', default=-1)


    @classmethod
    def get(cls, id):
        if id is None:
            group = KMGroup()
        else:
            group = super(KMGroup, cls).get(id=id)
        return group