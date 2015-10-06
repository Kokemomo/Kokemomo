from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, func
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from ..km_adapter import BaseAdapter

class BaseModel(object):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def __repr__(self):
        return '<%s>' % self.__class__.__name__

    def validate(self):
        pass

    def save(self, validate=True):
        if validate:
            self.validate()
        try:
            adapter.add(self)
            adapter.commit()
        except:
            adapter.rollback()
            raise

    def delete(self):
        try:
            adapter.delete(self)
            adapter.commit()
        except:
            adapter.rollback()
            raise

    @classmethod
    def all(cls):
        return adapter.session.query(cls).all()

    @classmethod
    def get(cls, id):
        return adapter.session.query(cls).filter(cls.id == id).first()

    @classmethod
    def delete(cls, id):
        try:
            elem = cls.get(id)
            adapter.delete(elem)
            adapter.commit()
        except:
            adapter.rollback()
            raise

    @classmethod
    def find(cls, **kwargs):
        return adapter.session.query(cls).filter_by(**kwargs).all()


class KMRDBAdapter(BaseAdapter):

    def __init__(self, rdb_path):
        self.rdb_path = rdb_path
        self.Model = declarative_base(cls=BaseModel)
        self.fields = [Column, String, Integer, Boolean, Text, DateTime]
        for field in self.fields:
            setattr(self, field.__name__, field)

    @property
    def metadata(self):
        return self.Model.metadata

    def init(self, rdb_path=None):
        self.session = scoped_session(sessionmaker())
        if rdb_path:
            self.rdb_path = rdb_path
        self.engine = create_engine(self.rdb_path, echo=True)
        self.session.configure(bind=self.engine)

        self.metadata.create_all(self.engine)

    def drop_all(self):
        self.metadata.drop_all(self.engine)

    def add(self, *args, **kwargs):
        self.session.add(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.session.delete(*args, **kwargs)

    def commit(self):
        self.session.commit()

    def set(self, *args, **kwargs):
        self.add(*args, **kwargs)
        self.commit()

    def rollback(self):
        self.session.rollback()

    def get(self, *args, **kwargs):
        pass

def rollback():
    adapter.session.rollback()

class Transaction(object):
    @classmethod
    def begin(cls):
        return adapter.session.begin(subtransactions=True)

    @classmethod
    def add(cls, *args, **kwargs):
        adapter.session.add(*args, **kwargs)

    @classmethod
    def commit(cls):
        adapter.session.commit()

    @classmethod
    def rollback(self):
        adapter.session.rollback()

from kokemomo.settings.common import DATA_BASE, STORAGE_ADAPTER_NAME

adapter = KMRDBAdapter(DATA_BASE)
