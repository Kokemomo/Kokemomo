#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.model.km_storage.impl.km_rdb_adapter import adapter

"""
It is the accessor to generic parameters table to be used in the KOKEMOMO.
[Table Layouts]
    id:Integer(Automatic Increment)
    key:String
    json:String
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
    key = adapter.Column(adapter.String(50), index=True, unique=True)
    json = adapter.Column(adapter.Text())

    def __repr__(self):
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)
