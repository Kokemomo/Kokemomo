#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.controller.km_db_manager import Base

__author__ = 'hiroki'

"""
It is blog subscription table to be used in the KOKEMOMO.
[Table Layouts]
    id:Integer
    user_id:Integer
    target_id:Integer
    create_at:DateTime(Automatic Updates)
    update_at:DateTime(Automatic Updates)

"""

class KMBlogSubscription(Base):
    __tablename__ = 'km_blog_subscription'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer)
    target_id = Column(Integer)
    create_at = Column(DateTime, default=datetime.datetime.now)
    update_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __repr__(self):
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)


def find(id, session):
    result = None
    for subscription in session.query(KMBlogSubscription).filter_by(id=id).all():
        result = subscription
    return result


def find_all(session):
    result = []
    fetch = session.query(KMBlogSubscription)
    for subscription in fetch.all():
        result.append(subscription)
    return result


def add(subscription, session):
    try:
        session.add(subscription)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def update(subscription, session):
    try:
        session.merge(subscription)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def delete(id, session):
    fetch_object = session.query(KMBlogSubscription).filter_by(id=id).one()
    try:
        session.delete(fetch_object)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
