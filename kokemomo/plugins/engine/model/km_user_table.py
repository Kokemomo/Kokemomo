#!/usr/bin/env python
# -*- coding:utf-8 -*-
import bcrypt
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.model.km_storage.impl.km_rdb_adapter import adapter
from kokemomo.settings import SETTINGS

__author__ = 'hiroki'

"""
It is the accessor to user table to be used in the KOKEMOMO.
[Table Layouts]
    id:Integer
    user_id:String
    name:String
    password:String
    mail_address:String
    group_id:Integer
    role_id:Integer
    create_at:DateTime(Automatic Updates)
    update_at:DateTime(Automatic Updates)

[Basic Usage]
You can use the each method from the acquisition of the session in getSession ().

-example-----------------------------------------------------------
from lib.kmusertable import get_session,add,find,find_all,delete

def search_parameter():
    session = get_session()
    result = find_all(session)
    session.close()
    return result

-------------------------------------------------------------------
"""


class KMUser(adapter.Model):
    __tablename__ = 'km_user'
    id = adapter.Column(adapter.Integer, autoincrement=True, primary_key=True)
    user_id = adapter.Column(adapter.String(20))
    name = adapter.Column(adapter.String(50))
    password = adapter.Column(adapter.String(20))
    mail_address = adapter.Column(adapter.String(254))
    group_id = adapter.Column(adapter.Integer)
    role_id = adapter.Column(adapter.Integer)

    def __repr__(self):
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)

    def save(self, validate=True):
        self.password = bcrypt.hashpw(self.password.encode(SETTINGS.CHARACTER_SET), bcrypt.gensalt())
        super(KMUser, self).save()
