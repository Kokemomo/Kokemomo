#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kokemomo.plugins.engine.utils.config import get_database_setting
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

__author__ = 'hiroki'

Base = declarative_base()

class KMDBManager():

    def __init__(self, name):
        self.initialize_session(name)

    def initialize_session(self, name):
        sql_url = get_database_setting(name)
        engine = create_engine(sql_url, encoding='utf-8', echo=True)
        self.Session = sessionmaker(bind=engine)
        Base.metadata.create_all(engine)

    def get_session(self):
        return self.Session()
