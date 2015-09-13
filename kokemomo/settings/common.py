#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hiroki-m'

WSGI_NAME='Bottle'
CHARACTER_SET = 'utf-8'
STORAGE_ADAPTER_NAME = 'SQLAlchemy'
TEST_LOGIN = True

## MySQL
DATA_BASE = 'mysql://root:mylocal@127.0.0.1:3306/kokemomo_test'
## sqlite:'sqlite:///data.db'


ADMIN_MENU = {
# name=url
    'ユーザー':'/admin/top?type=user',
    'グループ':'/admin/top?type=group',
    'ロール':'/admin/top?type=role',
    'パラメータ':'/admin/top?type=parameter',
    'ファイル':'/admin/top?type=file',
    'プラグイン':'/admin/top?type=plugin',
    'ログ':'/admin/top?type=log',
    'ブログ':'/blog/admin',
}


LOGGER = {
    'RotatingFileHandler':{
        'format':'%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        'filename':'kokemomo.log',
        'maxBytes':2000,
        'backupCount':5
    },
    'HTTPHandler':{
        'host':'localhost',
        'url':'/log',
        'method':'GET'
    }
}


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
    }
}