#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.controller.km_db_manager import Base
from sqlalchemy.types import Text

__author__ = 'hiroki'

"""
It is blog category table to be used in the KOKEMOMO.
[Table Layouts]
    id:Integer
    info_id:Integer
    name:Text
    create_at:DateTime(Automatic Updates)
    update_at:DateTime(Automatic Updates)

"""

class KMBlogCategory(Base):
    __tablename__ = 'km_blog_category'
    id = Column(Integer, autoincrement=True, primary_key=True)
    info_id = Column(Integer)
    name = Column(Text)
    create_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    update_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __repr__(self):
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)

def create(id, session):
    if id == 'None':
        category = KMBlogCategory()
        category.name = ""
    else:
        category = find(id, session)
    return category

def find(id, session):
    result = None
    for category in session.query(KMBlogCategory).filter_by(id=id).all():
        result = category
    return result

def find_by_info(info_id, session):
    result = []
    for info in session.query(KMBlogCategory).filter_by(info_id=info_id).all():
        result.append(info)
    return result

def find_all(session):
    result = []
    fetch = session.query(KMBlogCategory)
    for category in fetch.all():
        result.append(category)
    return result


def add(category, session):
    try:
        session.add(category)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def update(category, session):
    try:
        session.merge(category)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def delete(id, session):
    fetch_object = session.query(KMBlogCategory).filter_by(id=id).one()
    try:
        session.delete(fetch_object)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e

def delete_by_info(info_id, session):
    fetch = session.query(KMBlogCategory).filter_by(info_id=info_id).all()
    try:
        for target in fetch:
            session.delete(target)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e