#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.utils.config import get_database_setting

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


def add(group, session):
    """
    Add the group
    :param group: group model
    :param session: session
    """
    session.add(group)
    session.commit()


def update(group, session):
    """
    Update the group.
    :param group: group model
    :param session: session
    """
    session.merge(group)
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
