#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.controller.km_storage import db

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


class KMBlogSubscription(db.Model):
    __tablename__ = 'km_blog_subscription'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer)
    target_id = db.Column(db.Integer)

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
