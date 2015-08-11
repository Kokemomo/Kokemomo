#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.controller.km_storage import storage

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


class KMUser(storage.Model):
    __tablename__ = 'km_user'
    id = storage.Column(storage.Integer, autoincrement=True, primary_key=True)
    user_id = storage.Column(storage.String(20))
    name = storage.Column(storage.String(50))
    password = storage.Column(storage.String(20))
    mail_address = storage.Column(storage.String(254))
    group_id = storage.Column(storage.Integer)
    role_id = storage.Column(storage.Integer)

    def __repr__(self):
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)


def find(user_id, session):
    """
    Find the user.
    :param id: user id.
    :param session: session
    :return: user data.
    """
    result = None
    for user in session.query(KMUser).filter_by(user_id=user_id).all():
        result = user
    return result


def find_all(session):
    """
    Find all the users.
    :param session: session
    :return: user data.
    """
    result = []
    fetch = session.query(KMUser)
    for user in fetch.all():
        result.append(user)
    return result

def add(user, session):
    """
    Add the user.
    :param user: user model.
    :param session: session
    :return:
    """
    try:
        session.add(user)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def update(user, session):
    """
    Update the user.
    :param user: user model.
    :param session: session
    :return:
    """
    try:
        session.merge(user)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def delete(id, session):
    """
    Delete the user.
    :param id: user id
    :param session: session
    """
    fetch_object = session.query(KMUser).filter_by(id=id).one()
    try:
        session.delete(fetch_object)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e

