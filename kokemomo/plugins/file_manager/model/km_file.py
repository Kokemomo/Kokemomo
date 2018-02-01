#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from kokemomo.settings import SETTINGS
from kokemomo.plugins.engine.utils.km_utils import create_result

class KMFile:

    @classmethod
    def list(cls, data):
        dirs = []
        files = []
        for (root, dir_list, files) in os.walk(SETTINGS.DATA_DIR_PATH):
            for dir_name in dir_list:
                dir_path = root + os.sep + dir_name
                dirs.append(dir_path[len(SETTINGS.DATA_DIR_PATH):])
        files = os.listdir(SETTINGS.DATA_DIR_PATH + dirs[0])
        for file_name in files:
            if os.path.isdir(SETTINGS.DATA_DIR_PATH + os.sep + dirs[0] + os.sep + file_name):
                files.remove(file_name)
        return (dirs, files)

    @classmethod
    def upload(cls, data):
        directory_path = data.get_request_parameter('directory')
        files = data.get_request().files
        file_obj = files.get('files')
        file_name = file_obj.filename
        file_name = file_name
        save_path = os.path.join(SETTINGS.DATA_DIR_PATH + os.sep + directory_path, file_name)
        with open(save_path, "wb") as open_file:
            open_file.write(file_obj.file.read())
    #        logging.info("file upload. name=" + save_path);

    @classmethod
    def change_dir(cls, data):
        dirs = os.listdir(SETTINGS.DATA_DIR_PATH)
        # dir only
        for dir_name in dirs:
            if os.path.isfile(dir_name):
                dirs.remove(dir_name)
        files = []
        for selectDir in data.get_request().forms:
            files = os.listdir(SETTINGS.DATA_DIR_PATH + os.sep + selectDir)
        result = ""
        for file_name in files:
            if not file_name.startswith("."):
                result = result + file_name + ","
        result = result[0:len(result) - 1]
        return create_result(result)

    @classmethod
    def remove(cls, data):
        for remove_target in data.get_request().forms:
            target = remove_target.split(',')
            os.remove(SETTINGS.DATA_DIR_PATH + os.sep + target[0] + os.sep + target[1])
            print("remove. " + SETTINGS.DATA_DIR_PATH + os.sep + target[0] + os.sep + target[1])
