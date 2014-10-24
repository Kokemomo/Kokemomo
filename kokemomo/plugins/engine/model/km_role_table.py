#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.controller.km_db_manager import Base
from sqlalchemy.types import Boolean

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

class KMRole(Base):
    __tablename__ = 'km_role'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    target = Column(String(100))
    is_allow = Column(Boolean)
    create_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    update_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __repr__(self):
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)


def find(id, session):
    """
    Find the role.
    :param id: role id.
    :param session: session
    :return: role data.
    """
    result = None
    for role in session.query(KMRole).filter_by(id=id).all():
        result = role
    return result


def find_all(session):
    """
    Find all the roles.
    :param session: session
    :return: role data.
    """
    result = []
    fetch = session.query(KMRole)
    for role in fetch.all():
        result.append(role)
    return result


def add(role, session):
    """
    Add the role.
    :param role: role model
    :param session: session
    """
    try:
        session.add(role)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def update(role, session):
    """
    Update the role.
    :param role: role model
    :param session: session
    """
    try:
        session.merge(role)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def delete(id, session):
    """
    Delete the role.
    :param id: role id
    :param session: session
    """
    fetch_object = session.query(KMRole).filter_by(id=id).one()
    try:
        session.delete(fetch_object)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
