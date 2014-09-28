#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.utils.config import get_database_setting

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

def add(user, session):
    """
    Add the user.
    :param user: user model.
    :param session: session
    :return:
    """
    session.add(user)
    session.commit()


def update(user, session):
    """
    Update the user.
    :param user: user model.
    :param session: session
    :return:
    """
    session.merge(user)
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

