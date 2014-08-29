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
It is the accessor to group table to be used in the KOKEMOMO.
[Table Layouts]
    id:Integer
    name:String
    parent:String
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
Base = declarative_base()


class KMGroup(Base):
    __tablename__ = 'km_group'
    id = Column(String, primary_key=True)
    name = Column(String)
    parent_id = Column(String)
    create_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    update_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __repr__(self):
        if self.id is None:
            self.id = ''
        if self.name is None:
            self.name = ''
        if self.parent_id is None:
            self.parent_id = ''
        if self.create_at is None:
            self.create_at = ''
        if self.update_at is None:
            self.update_at = ''
        return "KMGroup<%s, %s, %s, %s, %s>" % (
            self.id, self.name, self.parent_id, str(self.create_at), str(self.update_at))

    def get_json(self):
        json = '{"id":"' +  str(self.id) + '"'
        if self.name is not None:
            json += ', "name":"' + self.name + '"'
        if self.parent_id is not None:
            json += ', "parent_id":"' + self.parent_id + '"'
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
    Find the group.
    :param id: group id.
    :param session: session
    :return: group data.
    """
    result = None
    for group in session.query(KMGroup).filter_by(id=id).all():
        result = group
    return result


def find_all(session):
    """
    Find all the groups.
    :param session: session
    :return: group data.
    """
    result = []
    fetch = session.query(KMGroup)
    for group in fetch.all():
        result.append(group)
    return result


def add(id, name, parent_id, session):
    """
    Add the group
    :param id: group id
    :param name:  group name
    :param parent_id:  group parent id
    :param session: session
    """
    group = KMGroup()
    group.id = id
    group.name = name
    group.parent_id = parent_id
    session.add(group)
    session.commit()


def update(id, name, parent_id, session):
    """
    Update the group.
    :param id: group id
    :param name: group name
    :param parent_id: group parent id
    :param session: session
    """
    fetch_object = session.query(KMGroup).filter(KMGroup.id == id).first()
    if type(fetch_object) is NoneType:
        add(id, name, parent_id, session)
    else:
        group_update = fetch_object
        group_update.name = name
        group_update.parent_id = parent_id
        session.add(group_update)
    session.commit()


def delete(id, session):
    """
    Delete the group.
    :param id: group id
    :param session: session
    """
    fetch_object = session.query(KMGroup).filter_by(id=id).one()
    session.delete(fetch_object)
    session.commit()
