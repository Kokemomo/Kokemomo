#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, json

from kokemomo.plugins.engine.controller.km_engine import KMEngine
from kokemomo.plugins.engine.controller.km_exception import log as log_error
from kokemomo.plugins.engine.controller.km_login import KMLogin

from kokemomo.plugins.engine.controller.km_session_manager import get_value_to_session
from kokemomo.plugins.engine.model.km_user_table import KMUser
from kokemomo.plugins.engine.model.km_group_table import KMGroup
from kokemomo.plugins.engine.model.km_role_table import KMRole
from kokemomo.plugins.engine.model.km_parameter_table import KMParameter

from kokemomo.settings import SETTINGS
from kokemomo.plugins.engine.utils.km_utils import get_menu_list
from kokemomo.plugins.engine.utils.km_utils import create_result, create_result_4_array


__author__ = 'hiroki-m'


DATA_DIR_PATH = "./kokemomo/data/test/"# TODO: 実行する場所によって変わる為、外部ファイルでHOMEを定義するような仕組みへ修正する


class KMAdmin(KMEngine):

    def get_name(self):
        return 'admin'


    def get_route_list(self):
        list = super(KMAdmin, self).get_route_list() # import engine route list
        list = list + (
            {'rule': '/admin-js/<filename>', 'method': 'GET', 'target': self.admin_js_static, 'name': 'admin_static_js'},
            {'rule': '/admin-css/<filename>', 'method': 'GET', 'target': self.admin_css_static, 'name': 'admin_static_css'},
            {'rule': '/admin-img/<filename>', 'method': 'GET', 'target': self.admin_img_static, 'name': 'admin_static_img'},
            {'rule': '/', 'method': 'GET', 'target': self.top},
            {'rule': '/login', 'method': 'GET', 'target': self.login},
            {'rule': '/login_auth', 'method': 'POST', 'target': self.login_auth},
            {'rule': '/logout', 'method': 'GET', 'target': self.logout},
            {'rule': '/top', 'method': 'GET', 'target': self.top},
            {'rule': '/user/save', 'method': 'POST', 'target': self.save_user},
            {'rule': '/user/search', 'method': 'GET', 'target': self.search_user},
            {'rule': '/group/save', 'method': 'POST', 'target': self.save_group},
            {'rule': '/group/search', 'method': 'GET', 'target': self.search_group},
            {'rule': '/role/save', 'method': 'POST', 'target': self.save_role},
            {'rule': '/role/search', 'method': 'GET', 'target': self.search_role},
            {'rule': '/parameter/save', 'method': 'POST', 'target': self.save_parameter},
            {'rule': '/parameter/search', 'method': 'GET', 'target': self.search_parameter},
            {'rule': '/file/upload', 'method': 'POST', 'target': self.upload},
            {'rule': '/file/remove', 'method': 'POST', 'target': self.remove_file},
            {'rule': '/file/change_dir', 'method': 'POST', 'target': self.select_dir},
        )
        return list


    def admin_js_static(self, filename):
        """
        set javascript files.
        :param filename: javascript file name.
        :return: static path.
        """
        return self.load_static_file(filename, root='kokemomo/plugins/admin/view/resource/js')


    def admin_css_static(self, filename):
        """
        set css files.
        :param filename: css file name.
        :return: static path.
        """
        return self.load_static_file(filename, root='kokemomo/plugins/admin/view/resource/css')


    def admin_img_static(self, filename):
        """
        set image files.
        :param filename: image file name.
        :return: static path.
        """
        return self.load_static_file(filename, root='kokemomo/plugins/admin/view/resource/img')


    def top(self):
        self.logger.debug("load top")
        type = self.data.get_request_parameter('type', default='info')
        menu_list = get_menu_list()
        user_id = self.data.get_user_id()
        dirs = []
        files = []
        if type == "file":
            for (root, dir_list, files) in os.walk(DATA_DIR_PATH):
                for dir_name in dir_list:
                    dir_path = root + os.sep + dir_name
                    dirs.append(dir_path[len(DATA_DIR_PATH):])
            files = os.listdir(DATA_DIR_PATH + dirs[0])
            for file_name in files:
                if os.path.isdir(DATA_DIR_PATH + os.sep + dirs[0] + os.sep + file_name):
                    files.remove(file_name)
        return self.render('kokemomo/plugins/admin/view/' + type, url=self.get_url, user_id=user_id, type=type, menu_list=menu_list, dirs=dirs, files=files)


    def login(self):
        return self.render('kokemomo/plugins/admin/view/login', url=self.get_url)


    def login_auth(self):
        return KMLogin.login_auth(self.data)


    def logout(self):
        KMLogin.logout(self.data)
        return self.render('kokemomo/plugins/admin/view/login', url=self.get_url)


    def save_user(self):
        """
        Save the user.
        will save the json string in the following formats.
        Format: 'keyName':{"hoge":"fuga"}

        """
        for save_user in self.data.get_request().forms:
            json_data = json.loads(save_user.decode(SETTINGS.CHARACTER_SET))
            for id in json_data:
                if json_data[id] == "":
                    KMUser.delete(id)
                else:
                    user = KMUser()
                    user.user_id = json_data[id]['user_id']
                    user.name = json_data[id]["name"]
                    user.password = json_data[id]["password"]
                    user.mail_address = json_data[id]["mail_address"]
                    user.group_id = json_data[id]["group_id"]
                    user.role_id = json_data[id]["role_id"]
                    user.save()


    def search_user(self):
        """
        Find all the user.
        :return: users.
        """
        result = KMUser.all()
        return create_result_4_array(result)



    def save_group(self):
        """
        Save the Group.
        will save the json string in the following formats.
        Format: 'keyName':{"hoge":"fuga"}

        """
        for save_group in self.data.get_request().forms:
            json_data = json.loads(save_group.decode(SETTINGS.CHARACTER_SET))
            for id in json_data:
                if json_data[id] == "":
                    KMGroup.delete(id)
                else:
                    group = KMGroup.get(id)
                    if not group:
                        group = KMGroup()
                    group.name = json_data[id]["name"]
                    group.parent_id = json_data[id]["parent_id"]
                    group.save()


    def search_group(self):
        """
        Find all the group.
        :return: groups.
        """
        result = KMGroup.all()
        return create_result_4_array(result)


    def save_role(self):
        """
        Save the role.
        will save the json string in the following formats.
        Format: 'keyName':{"hoge":"fuga"}

        """
        for save_group in self.data.get_request().forms:
            json_data = json.loads(save_group.decode(SETTINGS.CHARACTER_SET))
            for id in json_data:
                if json_data[id] == "":
                    KMRole.delete(id)
                else:
                    role = KMRole.get(id)
                    if not role:
                        role = KMRole()
                    role.name = json_data[id]["name"]
                    role.target = json_data[id]["target"]
                    role.is_allow = json_data[id]["is_allow"].lower() in ("true", "1")
                    role.save()


    def search_role(self):
        """
        Find all the role.
        :return: roles.
        """
        result = KMRole.all()
        return create_result_4_array(result)


    def save_parameter(self):
        """
        Save the parameter.
        will save the json string in the following formats.
        Format: 'keyName':{"hoge":"fuga"}

        """
        for save_params in self.data.get_request().forms:
            json_data = json.loads(save_params.decode(SETTINGS.CHARACTER_SET))
            for key in json_data:
                if json_data[key] == "":
                    KMParameter.delete(key)
                else:
                    parameters = KMParameter.find(key=key)
                    if not parameters:
                        parameter = KMParameter()
                    else:
                        parameter = parameter[0]
                    parameter.key = key
                    parameter.json = json_data[key]
                    parameter.save()


    def search_parameter(self):
        """
        Find all the parameters.
        :return: parameters.
        """
        result = KMParameter.all()
        return create_result_4_array(result)


    def upload(self):
        """
        Save the file that is specified in the request.
        """
        directory_path = self.data.get_request().forms.get('directory').decode(SETTINGS.CHARACTER_SET)
        data = self.data.get_request().files
        file_obj = data.get('files')
        file_name = file_obj.filename
        file_name = file_name.decode(SETTINGS.CHARACTER_SET)
        save_path = os.path.join(DATA_DIR_PATH + os.sep + directory_path, file_name)
        with open(save_path, "wb") as open_file:
            open_file.write(file_obj.file.read())
    #        logging.info("file upload. name=" + save_path);
        self.redirect("/admin/top")


    def remove_file(self):
        """
        Remove the file.
        """
        for remove_target in self.data.get_request().forms:
            target = remove_target.split(',')
            os.remove(DATA_DIR_PATH + os.sep + target[0] + os.sep + target[1])
            print("remove. " + DATA_DIR_PATH + os.sep + target[0] + os.sep + target[1])


    def select_dir(self):
        """
        Return the directory list for designated.

        example: If there is a dir1, dir2, dir3 in ". /data/(dir※)" directly under.
        ※Directory that is specified in the form.

        :return: "dir1,dir2,dir3"
        """
        dirs = os.listdir(DATA_DIR_PATH)
        # dir only
        for dir_name in dirs:
            if os.path.isfile(dir_name):
                dirs.remove(dir_name)
        files = []
        for selectDir in self.data.get_request().forms:
            files = os.listdir(DATA_DIR_PATH + os.sep + selectDir)
        result = ""
        for file_name in files:
            if not file_name.startswith("."):
                result = result + file_name + ","
        result = result[0:len(result) - 1]
        return create_result(result)
