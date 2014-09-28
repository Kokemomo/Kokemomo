#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.utils.config import get_database_setting

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
    is_allow = Column(String)
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
    session.add(role)
    session.commit()


def update(role, session):
    """
    Update the role.
    :param role: role model
    :param session: session
    """
    session.merge(role)
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
