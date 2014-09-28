#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.config import get_database_setting
from kokemomo.plugins.engine.utils.km_model_utils import *

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
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)

def get_session():
    """
    get database session.
    :return: session
    """
    sql_url = get_database_setting('engine')['url']
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


def add(history, session):
    """
    Add the history
    :param history: history model
    :param session: session
    """
    session.add(history)
    session.commit()


def update(history, session):
    """
    Update the history.
    :param history: history
    :param session: session
    """
    session.merge(history)
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
