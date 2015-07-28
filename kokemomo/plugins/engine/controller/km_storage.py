from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, func
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from abc import ABCMeta, abstractmethod

default_adapter = None


class Storage(object):
    def __init__(self, adapter=None):
        if adapter is None:
            self.adapter = default_adapter
        else:
            self.adapter = adapter

        if self.adapter.fields:
            for field in self.adapter.fields:
                setattr(self, field.__name__, field)

    def init(self, *args, **kwargs):
        self.adapter.init(*args, **kwargs)

    def set(self, *args, **kwargs):
        self.adapter.set(*args, **kwargs)

    def get(self, *args, **kwargs):
        return self.adapter.get(*args, **kwargs)

    @property
    def Model(self):
        return self.adapter.Model


class BasicAdapter(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def init(self, *args, **kwargs):
        pass

    @abstractmethod
    def set(self, *args, **kwargs):
        pass

    @abstractmethod
    def get(self, *args, **kwargs):
        pass


class RdbAdapter(object):
    __metaclass__ = ABCMeta


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
            db.adapter.add(self)
            db.adapter.commit()
        except:
            db.adapter.rollback()
            raise

    def delete(self):
        try:
            db.adapter.add(self)
            db.adapter.commit()
        except:
            db.adapter.rollback()
            raise

    @classmethod
    def all(cls):
        return db.session.query(cls)


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

from ..utils.km_config import get_database_setting


sql_url = get_database_setting('engine')
db = Storage(
    adapter=SQLAlchemyAdapter(sql_url)
)
# file = Storage(adapter=FileAdapter('~/hoge.md')
# redis = Storage(adapter=RedisAdapter())
