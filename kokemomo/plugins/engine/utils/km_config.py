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
    if section_name in __config_data:
        return __config_data[section_name]
    else:
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
                    __config_data[section_name] = database_schema
    return __config_data[section_name]

def get_database_pool_setting(name):
    '''
    get database pool setting.
    :param name: section name
    :return: config object
    '''
    section_name = 'Database_Pool_' + name
    settings = {}
    if section_name in __config_data:
        return __config_data[section_name]
    else:
        ini_file_path = os.path.abspath(os.curdir) + '/setting/kokemomo.ini'
        if os.path.exists(ini_file_path):
            config = ConfigParser.SafeConfigParser()
            config.read(ini_file_path)
            for section in config.sections():
                if section == section_name :
                    for option in config.options(section):
                        if option == 'recycle':
                            recycle = config.get(section, option)
                            settings['recycle'] = recycle
                    __config_data[section_name] = settings
    return __config_data[section_name]

def get_character_set_setting():
    '''
    get character set setting.
    :return: config object.
    '''
    section_name = 'Character_Set'
    if section_name in __config_data:
        return __config_data[section_name]
    else:
        ini_file_path = os.path.abspath(os.curdir) + '/setting/kokemomo.ini'
        if os.path.exists(ini_file_path):
            config = ConfigParser.SafeConfigParser()
            config.read(ini_file_path)
            for section in config.sections():
                if section == section_name :
                    for option in config.options(section):
                        if option == 'charset':
                            charset = config.get(section, option)
                    __config_data[section_name] = charset
    return __config_data[section_name]

def get_test_setting():
    '''
    get test setting.
    :return: config object.
    '''
    section_name = 'Test_Setting'
    settings = {}
    if section_name in __config_data:
        return __config_data[section_name]
    else:
        ini_file_path = os.path.abspath(os.curdir) + '/setting/kokemomo.ini'
        if os.path.exists(ini_file_path):
            config = ConfigParser.SafeConfigParser()
            config.read(ini_file_path)
            for section in config.sections():
                if section == section_name :
                    for option in config.options(section):
                        if option == 'test_login':
                            test_login = config.get(section, option)
                            settings['test_login'] = test_login
                    __config_data[section_name] = settings
    return __config_data[section_name]

def get_admin_menu_setting():
    '''
    get admin menu setting.
    :return: config object.
    '''
    section_name = 'Admin_Menu'
    settings = {}
    if section_name in __config_data:
        return __config_data[section_name]
    else:
        ini_file_path = os.path.abspath(os.curdir) + '/setting/kokemomo.ini'
        if os.path.exists(ini_file_path):
            config = ConfigParser.SafeConfigParser()
            config.read(ini_file_path)
            for section in config.sections():
                if section == section_name :
                    settings['menu'] = {}
                    for option in config.options(section):
                        menu_option = config.get(section, option)
                        settings['menu'][option] = menu_option
                    __config_data[section_name] = settings
    return __config_data[section_name]


def get_wsgi_setting():
    '''
    get wsgi setting.
    :return: config object.
    '''
    section_name = 'WSGI'
    if section_name in __config_data:
        return __config_data[section_name]
    else:
        ini_file_path = os.path.abspath(os.curdir) + '/setting/kokemomo.ini'
        if os.path.exists(ini_file_path):
            config = ConfigParser.SafeConfigParser()
            config.read(ini_file_path)
            for section in config.sections():
                if section == section_name :
                    for option in config.options(section):
                        if option == 'name':
                            name = config.get(section, option)
                    __config_data[section_name] = name
    return __config_data[section_name]


def get_logging_setting():
    '''
    get logging setting.
    :return: config object.
    '''
    section_name = 'Logging'
    settings = {}
    if section_name in __config_data:
        return __config_data[section_name]
    else:
        ini_file_path = os.path.abspath(os.curdir) + '/setting/kokemomo.ini'
        if os.path.exists(ini_file_path):
            config = ConfigParser.SafeConfigParser()
            config.read(ini_file_path)
            for section in config.sections():
                if section == section_name :
                    for option in config.options(section):
                        if option == 'level':
                            level = config.get(section, option)
                            settings['level'] = level
                        if option == 'format':
                            format = config.get(section, option)
                            settings['format'] = format
                        if option == 'handler':
                            handler = config.get(section, option)
                            settings['handler'] = handler
                        if option == 'filename':
                            filename = config.get(section, option)
                            settings['filename'] = filename
                        if option == 'maxbytes':
                            maxbytes = config.get(section, option)
                            settings['maxbytes'] = maxbytes
                        if option == 'backupcount':
                            backupcount = config.get(section, option)
                            settings['backupcount'] = backupcount
                    __config_data[section_name] = settings
    return __config_data[section_name]