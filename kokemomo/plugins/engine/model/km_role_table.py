#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy.schema import Column
from sqlalchemy import create_engine, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from types import *
import datetime

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
Base = declarative_base()


class KMRole(Base):
    __tablename__ = 'km_role'
    id = Column(String, primary_key=True)
    name = Column(String)
    target = Column(String)
    is_allow = Column(BooleanType)
    create_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    update_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __repr__(self):
        if self.id is None:
            self.id = ''
        if self.name is None:
            self.name = ''
        if self.target is None:
            self.target = ''
        if self.is_allow is None:
            self.is_allow = ''
        if self.create_at is None:
            self.create_at = ''
        if self.update_at is None:
            self.update_at = ''
        return "KMRole<%s, %s, %s, %s, %s, %s, %s>" % (
            self.id, self.name, self.target, self.is_allow, str(self.create_at), str(self.update_at))

    def get_json(self):
        json = '{"id":"' +  str(self.id) + '"'
        if self.name is not None:
            json += ', "name":"' + self.name + '"'
        if self.target is not None:
            json += ', "target":"' + self.target + '"'
        if self.is_allow is not None:
            json += ', "is_allow":"' + self.is_allow + '"'
        json += '}'
        return json

def get_session():
    """
    get database session.
    :return: session
    """
    sql_url = 'sqlite:///data.db'
    engine = create_engine(sql_url, encoding='utf-8', echo=True)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()


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


def add(id, name, target, is_allow, session):
    """
    Add the role.
    :param id: role id
    :param name:  role name
    :param target:  role target
    :param is_allow:  role is allow
    :param session: session
    """
    role = KMRole()
    role.id = id
    role.name = name
    role.target = target
    role.is_allow = is_allow
    session.add(role)
    session.commit()


def update(id, name, target, is_allow, session):
    """
    Update the role.
    :param id: role id
    :param name:  role name
    :param target:  role target
    :param is_allow:  role is allow
    :param session: session
    """
    fetch_object = session.query(KMRole).filter(KMRole.id == id).first()
    if type(fetch_object) is NoneType:
        add(id, name, target, is_allow, session)
    else:
        role_update = fetch_object
        role_update.name = name
        role_update.target = target
        role_update.is_allow = is_allow
        session.add(role_update)
    session.commit()


def delete(id, session):
    """
    Delete the role.
    :param id: role id
    :param session: session
    """
    fetch_object = session.query(KMRole).filter_by(id=id).one()
    session.delete(fetch_object)
    session.commit()
