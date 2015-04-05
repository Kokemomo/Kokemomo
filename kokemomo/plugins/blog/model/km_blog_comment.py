#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.controller.km_db_manager import Base
from sqlalchemy.types import Text

__author__ = 'hiroki'

"""
It is blog comment table to be used in the KOKEMOMO.
[Table Layouts]
    id:Integer
    article_id:Integer
    comment:Text
    create_at:DateTime(Automatic Updates)
    update_at:DateTime(Automatic Updates)

"""

class KMBlogComment(Base):
    __tablename__ = 'km_blog_comment'
    id = Column(Integer, autoincrement=True, primary_key=True)
    article_id = Column(Integer)
    comment = Column(Text)
    create_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    update_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __repr__(self):
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)


def find(id, session):
    result = None
    for comment in session.query(KMBlogComment).filter_by(id=id).all():
        result = comment
    return result


def find_all(session):
    result = []
    fetch = session.query(KMBlogComment)
    for comment in fetch.all():
        result.append(comment)
    return result


def add(comment, session):
    try:
        session.add(comment)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def update(comment, session):
    try:
        session.merge(comment)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def delete(id, session):
    fetch_object = session.query(KMBlogComment).filter_by(id=id).one()
    try:
        session.delete(fetch_object)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
