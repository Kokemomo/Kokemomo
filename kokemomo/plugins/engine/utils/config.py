#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'hiroki'

import os
import sys
import ConfigParser

root_path = os.path.abspath(os.pardir)
if not (root_path in sys.path):
    sys.path.append(root_path)

__config_data = {}

def get_database_setting(name):
    """
    parse configuration file.
    [key list]
    url : database schema url
    :return: config object
    """
    section_name = 'Database_' + name
    db_user_id = None
    password = None
    host = None
    port = None
    schema = None
    charset = None
    if not __config_data:
        ini_file_path = os.path.abspath(os.curdir) + '/setting/kokemomo.ini'
        if os.path.exists(ini_file_path):
            config = ConfigParser.SafeConfigParser()
            config.read(ini_file_path)
            for section in config.sections():
                if section == section_name :
                    for option in config.options(section):
                        if option == 'rdbms':
                            rdbms = config.get(section, option)
                        elif option == 'host':
                            host = config.get(section, option)
                        elif option == 'port':
                            port = config.get(section, option)
                        elif option == 'user_id':
                            db_user_id = config.get(section, option)
                        elif option == 'password':
                            password = config.get(section, option)
                        elif option == 'schema':
                            schema = config.get(section, option)
                        elif option == 'charset':
                            charset = config.get(section, option)
                    database_schema = ''
                    database_schema += rdbms
                    if rdbms == 'sqlite':
                        database_schema += ':///'
                    else:
                        database_schema += '://'
                    if db_user_id is not None:
                        database_schema += db_user_id
                        database_schema += ':'
                    if password is not None:
                        database_schema += password
                        database_schema += '@'
                    if host is not None:
                        database_schema += host
                        database_schema += ':'
                    if port is not  None:
                        database_schema += port
                        database_schema += '/'
                    if schema is not None:
                        database_schema += schema
                    if charset is not None:
                        database_schema += '?charset='
                        database_schema += charset
                    __config_data['url'] = database_schema
    return __config_data
