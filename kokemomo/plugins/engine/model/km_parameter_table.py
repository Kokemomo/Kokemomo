#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.model.km_storage.impl.km_rdb_adapter import adapter

"""
It is the accessor to generic parameters table to be used in the KOKEMOMO.
[Table Layouts]
    id:Integer(Automatic Increment)
    key:String
    data:String
    create_at:DateTime(Automatic Updates)
    update_at:DateTime(Automatic Updates)

[Basic Usage]
You can use the each method from the acquisition of the session in getSession ().

-example-----------------------------------------------------------
from lib.kmparametertable import get_session,add,find,find_all,delete

def search_parameter():
    session = get_session()
    result = find_all(session)
    session.close()
    return result

-------------------------------------------------------------------
"""


class KMParameter(adapter.Model):
    __tablename__ = 'km_parameter'
    id = adapter.Column(adapter.Integer, autoincrement=True, primary_key=True)
    key = adapter.Column(adapter.String(254), index=True, unique=True)
    data = adapter.Column(adapter.Text())


    def __init__(self, data=None):
        if data is None:
            self.key = ''
            self.data = '{}'
        else:
            self.set_data(data)


    def __repr__(self):
        return create_repr_str(self)


    def get_json(self):
        return create_json(self)


    def set_data(self, data):
        self.error = None
        self.key = data.get_request_parameter('key', default='')
        self.data = data.get_request_parameter('data', default='{}')


    @classmethod
    def get(cls, id):
        if id is None:
            parameter = KMParameter()
        else:
            parameter = super(KMParameter, cls).get(id=id)
        return parameter