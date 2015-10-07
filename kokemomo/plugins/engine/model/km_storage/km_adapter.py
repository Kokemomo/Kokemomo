from abc import ABCMeta, abstractmethod, abstractproperty

class BaseAdapter(object):
    __metaclass__ = ABCMeta

    #@abstractproperty
    #def Model(self):
    #    pass

    @abstractmethod
    def init(self, *args, **kwargs):
        pass

    #@abstractmethod
    #def set(self, *args, **kwargs):
    #    pass

    #@abstractmethod
    #def get(self, *args, **kwargs):
    #    pass
