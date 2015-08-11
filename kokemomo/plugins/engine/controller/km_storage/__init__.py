
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


from kokemomo.plugins.engine.utils.km_config import (
    get_database_setting,
    get_storage_adapter_setting
)

sql_url = get_database_setting('engine')
adapter_name = get_storage_adapter_setting()
adapter_filename = adapter_name.lower() + "_adapter"

mod = __import__(
    "kokemomo.plugins.engine.controller.km_storage.adapter",
    fromlist=[adapter_filename])
class_def = getattr(getattr(mod, adapter_filename), adapter_name+"Adapter")


db = Storage(
    adapter=class_def(sql_url)
)

__all__ = ['Storage', 'BasicAdapter', 'RdbAdapter', 'db']
