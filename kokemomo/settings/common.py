#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hiroki-m'

VERSION = 'Beta-0.1.2'

# Common
BACKEND_NAME='WSGI_Bottle'
SERVER='dev' # dev, gunicorn
WORKERS=1
HOST_NAME = 'localhost'
PORT = 8861
CHARACTER_SET = 'utf-8'
STORAGE_ADAPTER_NAME = 'SQLAlchemy'
TEST_LOGIN = True
DEBUG = False
RELOAD = False

# DATABASE
## MySQL
##DATA_BASE = 'mysql://user:pass@127.0.0.1:3306/dbname'
##DATA_BASE_OPTIONS = {
##    'echo': True,
##    'pool_recycle': 3600,
##}
## SQLite
DATA_BASE = 'sqlite:///data.db'
DATA_BASE_OPTIONS = {}

# ADMIN
ADMIN_MENU = {
# name=url
    'ユーザー':'/admin/user',
    'グループ':'/admin/group',
    'ロール':'/admin/role',
    'パラメータ':'/admin/parameter',
    'ファイル':'/admin/file',
    'プラグイン':'/admin/plugin',
#    'ログ':'/admin/log',
    'ブログ':'/blog/admin',
}


# LOGGING
LOGGER = {
    'RotatingFileHandler':{
        'format':'%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        'filename':'kokemomo.log',
        'maxBytes':2000000,
        'backupCount':5
    },
    'HTTPHandler':{
        'host':'localhost',
        'url':'/log',
        'method':'GET'
    }
}

# PLUGINS
PLUGINS = {
    'kokemomo':{
        'logger':'RotatingFileHandler',
        'level':'INFO'
    },
    'admin':{
        'logger':'RotatingFileHandler',
        'level':'INFO'
    },
    'engine':{
        'logger':'RotatingFileHandler',
        'level':'INFO'
    },
    'blog':{
        'logger':'RotatingFileHandler',
        'level':'INFO'
    }
}

# BLOG
BLOG_TEMPLATE = "normal"

#
DATA_DIR_PATH = "./kokemomo/data/test/"
