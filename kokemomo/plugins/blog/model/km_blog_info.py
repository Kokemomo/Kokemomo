#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.controller.km_storage import storage

__author__ = 'hiroki'

"""
It is blog information table to be used in the Kokemomo.
[Table Layouts]
    id:Integer
    name:Text
    url:Text
    description:Text
    create_at:DateTime(Automatic Updates)
    update_at:DateTime(Automatic Updates)
"""


class KMBlogInfo(storage.Model):
    __tablename__ = 'km_blog_info'
    id = storage.Column(storage.Integer, autoincrement=True, primary_key=True)
    name = storage.Column(storage.Text)
    url = storage.Column(storage.Text)
    description = storage.Column(storage.Text)

    def __repr__(self):
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)


def create(id, session):
    if id == 'None':
        info = KMBlogInfo()
        info.name = ""
        info.url = ""
        info.description = ""
    else:
        info = find(id, session)
    return info


# def find(id, session):
#     result = None
#     for info in session.query(KMBlogInfo).filter_by(id=id).all():
#         result = info
#     return result
#
#
# def find_by_url(url, session):
#     result = None
#     for info in session.query(KMBlogInfo).filter_by(url=url).all():
#         result = info
#     return result
#
#
# def find_all(session):
#     result = []
#     fetch = session.query(KMBlogInfo)
#     for info in fetch.all():
#         result.append(info)
#     return result
#
#
# def add(info, session):
#     try:
#         session.add(info)
#         session.commit()
#     except Exception as e:
#         session.rollback()
#         raise e
#
#
# def update(info, session):
#     try:
#         session.merge(info)
#         session.commit()
#     except Exception as e:
#         session.rollback()
#         raise e
#
#
# def delete(id, session):
#     fetch_object = session.query(KMBlogInfo).filter_by(id=id).one()
#     try:
#         session.delete(fetch_object)
#         session.commit()
#     except Exception as e:
#         session.rollback()
#         raise e
