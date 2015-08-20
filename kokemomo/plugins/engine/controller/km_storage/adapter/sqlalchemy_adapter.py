from sqlalchemy import (
    Column, Integer, String, Text, DateTime, Boolean, func
)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from kokemomo.plugins.engine.controller.km_storage import *


class BaseModel(object):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def __repr__(self):
        return '<%s>' % self.__class__.__name__

    def save(self):
        try:
            storage.adapter.add(self)
            storage.adapter.commit()
        except:
            storage.adapter.rollback()
            raise

    def delete(self):
        try:
            storage.adapter.add(self)
            storage.adapter.commit()
        except:
            storage.adapter.rollback()
            raise

    @classmethod
    def all(cls):
        return storage.session.query(cls)


class SQLAlchemyAdapter(BasicAdapter, RdbAdapter):

    def __init__(self, db_path):
        self.session = scoped_session(sessionmaker())
        self.engine = create_engine(db_path, echo=True)
        self.Model = declarative_base(cls=BaseModel)
        self.session.configure(bind=self.engine)

        self.fields = [Column, String, Text, Integer, Boolean, DateTime]

    @property
    def metadata(self):
        return self.Model.metadata

    def init(self):
        self.metadata.create_all(self.engine)

    def drop_all(self):
        self.metadata.drop_all(self.engine)

    def add(self, *args, **kwargs):
        self.session.add(*args, **kwargs)

    def commit(self):
        self.session.commit()

    def set(self, *args, **kwargs):
        self.add(*args, **kwargs)
        self.commit()

    def rollback(self):
        self.session.rollback()

    def get(self, *args, **kwargs):
        pass
