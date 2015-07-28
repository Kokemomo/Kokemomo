#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.controller.km_storage import db
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


class KMBlogComment(db.Model):
    __tablename__ = 'km_blog_comment'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    article_id = db.Column(db.Integer)
    comment = db.Column(db.Text)

    def __repr__(self):
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)


def find(id, session):
    result = None
    for comment in session.query(KMBlogComment).filter_by(id=id).all():
        result = comment
    return result


def find_by_article_id(article_id, session):
    result = []
    fetch = session.query(KMBlogComment).filter_by(article_id=article_id).all()
    for comment in fetch:
        result.append(comment)
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
