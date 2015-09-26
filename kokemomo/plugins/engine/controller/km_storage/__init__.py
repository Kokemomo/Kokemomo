from .impl.km_rdb_adapter import adapter

def initialize():
    adapter.init()

class Storage(object):
    def Column(self):
        pass

storage = Storage()
