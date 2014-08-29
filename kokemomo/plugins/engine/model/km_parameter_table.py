#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy.schema import Column
from sqlalchemy import create_engine, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from types import *
import datetime

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
Base = declarative_base()


class KMParameter(Base):
    __tablename__ = 'km_parameter'
    id = Column(Integer, autoincrement=True, primary_key=True)
    key = Column(String)
    json = Column(String)
    create_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    update_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __repr__(self):
        if self.id is None:
            self.id = ''
        if self.key is None:
            self.key = ''
        if self.json is None:
            self.json = ''
        if self.create_at is None:
            self.create_at = ''
        if self.update_at is None:
            self.update_at = ''
        return "KMParameter<%d, %s, %s, %s, %s>" % (
            self.id, self.key, self.json, str(self.create_at), str(self.update_at))

    def get_json(self):
        json = '{"id":"' +  str(self.id) + '"'
        if self.key is not None:
            json += ', "key":"' + self.key + '"'
        if self.json is not None:
            json += ', "json":' + self.json + ''
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


def find(key, session):
    """
    Find the parameter.
    :param key: parameter key name.
    :param session: session
    :return: parameter data.
    """
    result = None
    for parameter in session.query(KMParameter).filter_by(key=key).all():
        result = parameter
    return result


def find_all(session):
    """
    Find all the parameters.
    :param session: session
    :return: parameter data.
    """
    result = []
    fetch = session.query(KMParameter)
    for parameter in fetch.all():
        result.append(parameter)
    return result


def add(key, json, session):
    """
    Add the parameter.
    :param key: parameter key name
    :param json:  parameter data
    :param session: session
    """
    parameter = KMParameter()
    parameter.key = key
    parameter.json = json
    session.add(parameter)
    session.commit()


def update(key, json, session):
    """
    Update the parameter.
    :param key: parameter key name
    :param json: parameter data
    :param session: session
    """
    fetch_object = session.query(KMParameter).filter(KMParameter.key == key).first()
    if type(fetch_object) is NoneType:
        add(key, json, session)
    else:
        param_update = fetch_object
        param_update.json = json
        session.add(param_update)
    session.commit()


def delete(key, session):
    """
    Delete the parameter.
    :param key: parameter key name
    :param session: session
    """
    fetch_object = session.query(KMParameter).filter_by(key=key).one()
    session.delete(fetch_object)
    session.commit()
