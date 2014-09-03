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
It is the accessor to history table to be used in the KOKEMOMO.
[Table Layouts]
    id:Integer
    user_id:Integer
    contents:String
    count:Integer
    create_at:DateTime(Automatic Updates)
    update_at:DateTime(Automatic Updates)

[Basic Usage]
You can use the each method from the acquisition of the session in getSession ().

-example-----------------------------------------------------------
from lib.kmhistorytable import get_session,add,find,find_all,delete

def search_parameter():
    session = get_session()
    result = find_all(session)
    session.close()
    return result

-------------------------------------------------------------------
"""
Base = declarative_base()


class KMHistory(Base):
    __tablename__ = 'km_group'
    id = Column(String, primary_key=True)
    user_id = Column(String)
    contents = Column(String)
    count = Column(String)
    create_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    update_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __repr__(self):
        if self.id is None:
            self.id = ''
        if self.user_id is None:
            self.user_id = ''
        if self.contents is None:
            self.contents = ''
        if self.count is None:
            self.count = ''
        if self.create_at is None:
            self.create_at = ''
        if self.update_at is None:
            self.update_at = ''
        return "KMHistory<%s, %s, %s, %s, %s>" % (
            self.id, self.user_id, self.count, str(self.create_at), str(self.update_at))

    def get_json(self):
        json = '{"id":"' +  str(self.id) + '"'
        if self.user_id is not None:
            json += ', "user_id":"' + self.user_id + '"'
        if self.contents is not None:
            json += ', "contents":"' + self.contents + '"'
        if self.count is not None:
            json += ', "count":"' + self.count + '"'
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

def find(user_id, session):
    """
    Find all the history.
    :param user_id: history user_id
    :param session: session
    :return: history data.
    """
    result = []
    fetch = session.query(KMHistory)
    for history in fetch.filter_by(user_id=user_id).all():
        result.append(history)
    return result


def find_list(number_of_weeks, session):
    """
    Find all the history.
    :param number_of_weeks: A few weeks ago
    :param session: session
    :return: history data.
    """
    result = []
    fetch = session.query(KMHistory)
    current_time = datetime.datetime.utcnow()
    point_in_time = current_time - datetime.timedelta(weeks=number_of_weeks)
    for history in fetch.filter(KMHistory.update_at > point_in_time).all():
        result.append(history)
    return result


def add(id, user_id, contents, count, session):
    """
    Add the history
    :param id: history id
    :param user_id:  history user_id
    :param contents:  history contents
    :param count:  history count
    :param session: session
    """
    history = KMHistory()
    history.id = id
    history.user_id = user_id
    history.contents = contents
    history.count = count
    session.add(history)
    session.commit()


def update(id, user_id, contents, count, session):
    """
    Update the history.
    :param id: history id
    :param user_id:  history user_id
    :param contents:  history contents
    :param count:  history count
    :param session: session
    """
    fetch_object = session.query(KMHistory).filter(KMHistory.id == id).first()
    if type(fetch_object) is NoneType:
        add(id, user_id, contents, count, session)
    else:
        history_update = fetch_object
        history_update.user_id = user_id
        history_update.contents = contents
        history_update.count = count
        session.add(history_update)
    session.commit()


def delete(id, session):
    """
    Delete the history.
    :param id: history id
    :param session: session
    """
    fetch_object = session.query(KMHistory).filter_by(id=id).one()
    session.delete(fetch_object)
    session.commit()
