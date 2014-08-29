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
It is the accessor to user table to be used in the KOKEMOMO.
[Table Layouts]
    id:Integer
    name:String
    password:String
    mail_address:String
    group_id:String
    role_id:String
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
Base = declarative_base()


class KMUser(Base):
    __tablename__ = 'km_user'
    id = Column(String, primary_key=True)
    name = Column(String)
    password = Column(String)
    mail_address = Column(String)
    group_id = Column(String)
    role_id = Column(String)
    create_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    update_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __repr__(self):
        if self.id is None:
            self.id = ''
        if self.name is None:
            self.name = ''
        if self.password is None:
            self.password = ''
        if self.mail_address is None:
            self.mail_address = ''
        if self.group_id is None:
            self.group_id = ''
        if self.group_id is None:
            self.group_id = ''
        if self.role_id is None:
            self.role_id = ''
        if self.create_at is None:
            self.create_at = ''
        if self.update_at is None:
            self.update_at = ''
        return "KMUser<%s, %s, %s, %s, %s, %s, %s, %s>" % (
            self.id, self.name, self.password, self.mail_address, self.group_id, self.role_id, str(self.create_at), str(self.update_at))

    def get_json(self):
        json = '{"id":"' +  str(self.id) + '"'
        if self.name is not None:
            json += ', "name":"' + self.name + '"'
        if self.password is not None:
            json += ', "password":"' + self.password + '"'
        if self.mail_address is not None:
            json += ', "mail_address":"' + self.mail_address + '"'
        if self.group_id is not None:
            json += ', "group_id":"' + self.group_id + '"'
        if self.role_id is not None:
            json += ', "role_id":"' + self.role_id + '"'
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
    Find the user.
    :param id: user id.
    :param session: session
    :return: user data.
    """
    result = None
    for user in session.query(KMUser).filter_by(id=id).all():
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


def add(id, name, password, mail_address, group_id, role_id, session):
    """
    Add the user.
    :param id: user id
    :param name:  user name
    :param password:  user password
    :param mail_address:  user mail address
    :param group_id:  user group id
    :param role_id:  user role id
    :param session: session
    """
    user = KMUser()
    user.id = id
    user.name = name
    user.password = password
    user.mail_address = mail_address
    user.group_id = group_id
    user.role_id = role_id
    session.add(user)
    session.commit()


def update(id, name, password, mail_address, group_id, role_id, session):
    """
    Update the user.
    :param id: user id
    :param name:  user name
    :param password:  user password
    :param mail_address:  user mail address
    :param group_id:  user group id
    :param role_id:  user role id
    :param session: session
    """
    fetch_object = session.query(KMUser).filter(KMUser.id == id).first()
    if type(fetch_object) is NoneType:
        add(id, name, password, mail_address, group_id, role_id, session)
    else:
        user_update = fetch_object
        user_update.name = name
        user_update.password = password
        user_update.mail_address = mail_address
        user_update.group_id = group_id
        user_update.role_id = role_id
        session.add(user_update)
    session.commit()


def delete(id, session):
    """
    Delete the user.
    :param id: user id
    :param session: session
    """
    fetch_object = session.query(KMUser).filter_by(id=id).one()
    session.delete(fetch_object)
    session.commit()
