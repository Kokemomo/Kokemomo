__author__ = 'hiroki-m'

import sys

DEFAULT_SETTING_FILE='kokemomo.settings'
setting_name = 'common'


argc = len(sys.argv)
if argc > 1:
    argv_list = sys.argv
    for index, value in enumerate(argv_list):
        if value == '-s':
            setting_name = argv_list[index+1]

mod = __import__(DEFAULT_SETTING_FILE, fromlist=[setting_name])
SETTINGS = getattr(mod, setting_name)
