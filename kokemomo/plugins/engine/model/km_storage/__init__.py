from kokemomo.plugins.engine.model.km_storage.impl.km_rdb_adapter import adapter

def initialize(rdb_path=None):
    adapter.init(rdb_path)

class Storage(object):
    def Column(self):
        pass

storage = Storage()
