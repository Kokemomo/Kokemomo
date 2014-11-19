#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kokemomo.plugins.engine.utils.config import get_database_setting, get_database_pool_setting, get_character_set_setting
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
        pool_settings = get_database_pool_setting(name)
        charset = get_character_set_setting()
        if 'recycle' in pool_settings:
            engine = create_engine(sql_url, encoding=charset, echo=True, pool_recycle=pool_settings['recycle'])
        else:
            engine = create_engine(sql_url, encoding=charset, echo=True)
        self.Session = sessionmaker(bind=engine)
        Base.metadata.create_all(engine)

    def get_session(self):
        return self.Session()
