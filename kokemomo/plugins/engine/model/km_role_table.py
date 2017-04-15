#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.model.km_storage.impl.km_rdb_adapter import adapter

__author__ = 'hiroki'

"""
It is the accessor to role table to be used in the KOKEMOMO.
[Table Layouts]
    id:Integer
    name:String
    target:String
    is_allow:Boolean
    create_at:DateTime(Automatic Updates)
    update_at:DateTime(Automatic Updates)

[Basic Usage]
You can use the each method from the acquisition of the session in getSession ().

-example-----------------------------------------------------------
from lib.kmroletable import get_session,add,find,find_all,delete

def search_parameter():
    session = get_session()
    result = find_all(session)
    session.close()
    return result

-------------------------------------------------------------------
"""


class KMRole(adapter.Model):
    __tablename__ = 'km_role'
    id = adapter.Column(adapter.Integer, autoincrement=True, primary_key=True)
    name = adapter.Column(adapter.String(50))
    target = adapter.Column(adapter.String(100))
    is_allow = adapter.Column(adapter.Boolean)


    def __init__(self, data=None):
        if data is None:
            self.name = ''
            self.target = ''
            self.is_allow = False
        else:
            self.set_data(data)


    def __repr__(self):
        return create_repr_str(self)


    def get_json(self):
        return create_json(self)


    def set_data(self, data):
        self.error = None
        self.name = data.get_request_parameter('name', default='')
        self.target = data.get_request_parameter('target', default='')
        self.is_allow = data.get_request_parameter('is_allow', default=False)


    @classmethod
    def get(cls, id):
        if id is None:
            role = KMRole()
        else:
            role = super(KMRole, cls).get(id=id)
        return role