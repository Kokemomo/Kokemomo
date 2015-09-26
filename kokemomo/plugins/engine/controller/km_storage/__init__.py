from .impl.km_rdb_adapter import adapter

def initialize():
    adapter.init()

class Storage(object):
    def Column(self):
        pass

storage = Storage()
#from kokemomo.settings.common import DATA_BASE, STORAGE_ADAPTER_NAME
#
#sql_url = DATA_BASE
#adapter_name = STORAGE_ADAPTER_NAME
#adapter_filename = adapter_name.lower() + "_adapter"
#
#mod = __import__(
#    "kokemomo.plugins.engine.controller.km_storage.adapter",
#    fromlist=[adapter_filename])
#class_def = getattr(getattr(mod, adapter_filename), adapter_name+"Adapter")
#
#
#storage = Storage(
#    adapter=class_def(sql_url)
#)
#
#__all__ = ['Storage', 'BasicAdapter', 'RdbAdapter', 'storage']
