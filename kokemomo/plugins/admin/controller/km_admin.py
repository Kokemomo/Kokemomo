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
from kokemomo.plugins.admin.model.km_user_admin import KMUserAdmin
from kokemomo.plugins.admin.model.km_parameter_admin import KMParameterAdmin

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
            {'rule': '/', 'method': 'GET', 'target': self.admin_info},
            {'rule': '/login', 'method': 'GET', 'target': self.login},
            {'rule': '/login_auth', 'method': 'POST', 'target': self.login_auth},
            {'rule': '/logout', 'method': 'GET', 'target': self.logout},
            {'rule': '/top', 'method': 'GET', 'target': self.admin_info},
            {'rule': '/user', 'method': 'GET', 'target': self.admin_user},
            {'rule': '/user/edit', 'method': 'GET', 'target': self.admin_user_edit},
            {'rule': '/user/save', 'method': 'POST', 'target': self.admin_user_save},
            {'rule': '/group', 'method': 'GET', 'target': self.admin_group},
            {'rule': '/group/edit', 'method': 'GET', 'target': self.admin_group_edit},
            {'rule': '/group/save', 'method': 'POST', 'target': self.admin_group_save},
            {'rule': '/role', 'method': 'GET', 'target': self.admin_role},
            {'rule': '/role/edit', 'method': 'GET', 'target': self.admin_role_edit},
            {'rule': '/role/save', 'method': 'POST', 'target': self.admin_role_save},
            {'rule': '/parameter', 'method': 'GET', 'target': self.admin_parameter},
            {'rule': '/parameter/edit', 'method': 'GET', 'target': self.admin_parameter_edit},
            {'rule': '/parameter/save', 'method': 'POST', 'target': self.admin_parameter_save},
            {'rule': '/file', 'method': 'GET', 'target': self.admin_file},
            {'rule': '/file/upload', 'method': 'POST', 'target': self.admin_file_upload},
            {'rule': '/file/remove', 'method': 'POST', 'target': self.admin_file_remove},
            {'rule': '/file/change_dir', 'method': 'POST', 'target': self.admin_select_dir},
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


    @log_error
    @KMEngine.action('kokemomo/plugins/admin/view/info')
    def admin_info(self):
        '''
        admin info page
        :return: template
        '''
        self.result['menu_list'] = get_menu_list()


    @log_error
    @KMEngine.action('kokemomo/plugins/admin/view/file')
    def admin_file(self):
        dirs = []
        files = []
        for (root, dir_list, files) in os.walk(DATA_DIR_PATH):
            for dir_name in dir_list:
                dir_path = root + os.sep + dir_name
                dirs.append(dir_path[len(DATA_DIR_PATH):])
        files = os.listdir(DATA_DIR_PATH + dirs[0])
        for file_name in files:
            if os.path.isdir(DATA_DIR_PATH + os.sep + dirs[0] + os.sep + file_name):
                files.remove(file_name)
        self.result['menu_list'] = get_menu_list()
        self.result['dirs'] = dirs
        self.result['files'] = files

    @log_error
    @KMEngine.action('kokemomo/plugins/admin/view/user_list')
    def admin_user(self):
        '''
        admin user page
        :return: template
        '''
        self.result['menu_list'] = get_menu_list()
        self.result['users'] = KMUser.all()


    @log_error
    @KMEngine.action('kokemomo/plugins/admin/view/user_edit')
    def admin_user_edit(self):
        '''
        admin user page
        :return: template
        '''
        id = self.data.get_request_parameter("km_user_edit_id");
        self.result['menu_list'] = get_menu_list()
        self.result['user'] = KMUser.get(id)
        self.result['groups'] = KMGroup.all()
        self.result['roles'] = KMRole.all()


    @log_error
    @KMEngine.action('kokemomo/plugins/admin/view/user_list')
    def admin_user_save(self):
        '''
        admin user page
        :return: template
        '''
        KMUserAdmin.save_user(self.data)
        self.result['menu_list'] = get_menu_list()
        self.result['users'] = KMUser.all()

    @log_error
    @KMEngine.action('kokemomo/plugins/admin/view/group_list')
    def admin_group(self):
        '''
        admin group page
        :return: template
        '''
        self.result['menu_list'] = get_menu_list()
        self.result['groups'] = KMGroup.all()


    @log_error
    @KMEngine.action('kokemomo/plugins/admin/view/group_edit')
    def admin_group_edit(self):
        '''
        admin group page
        :return: template
        '''
        id = self.data.get_request_parameter("km_group_edit_id");
        self.result['menu_list'] = get_menu_list()
        self.result['group'] = KMGroup.get(id)
        self.result['groups'] = KMGroup.all()


    @log_error
    @KMEngine.action('kokemomo/plugins/admin/view/group_list')
    def admin_group_save(self):
        '''
        admin group page
        :return: template
        '''
        KMUserAdmin.save_group(self.data)
        self.result['menu_list'] = get_menu_list()
        self.result['groups'] = KMGroup.all()

    @log_error
    @KMEngine.action('kokemomo/plugins/admin/view/role_list')
    def admin_role(self):
        '''
        admin role page
        :return: template
        '''
        self.result['menu_list'] = get_menu_list()
        self.result['roles'] = KMRole.all()


    @log_error
    @KMEngine.action('kokemomo/plugins/admin/view/role_edit')
    def admin_role_edit(self):
        '''
        admin role page
        :return: template
        '''
        id = self.data.get_request_parameter("km_role_edit_id");
        self.result['menu_list'] = get_menu_list()
        self.result['role'] = KMRole.get(id)


    @log_error
    @KMEngine.action('kokemomo/plugins/admin/view/role_list')
    def admin_role_save(self):
        '''
        admin user page
        :return: template
        '''
        KMUserAdmin.save_role(self.data)
        self.result['menu_list'] = get_menu_list()
        self.result['roles'] = KMRole.all()


    def login(self):
        return self.render('kokemomo/plugins/admin/view/login', url=self.get_url)


    def login_auth(self):
        return KMLogin.login_auth(self.data)


    def logout(self):
        KMLogin.logout(self.data)
        return self.render('kokemomo/plugins/admin/view/login', url=self.get_url)


    @log_error
    @KMEngine.action('kokemomo/plugins/admin/view/parameter_list')
    def admin_parameter(self):
        """
        Find all the parameters.
        :return: parameters.
        """
        self.result['menu_list'] = get_menu_list()
        self.result['parameters'] = KMParameter.all()

    @log_error
    @KMEngine.action('kokemomo/plugins/admin/view/parameter_edit')
    def admin_parameter_edit(self):
        id = self.data.get_request_parameter("km_parameter_edit_id")
        self.result['menu_list'] = get_menu_list()
        self.result['parameter'] = KMParameter.get(id)

    @log_error
    @KMEngine.action('kokemomo/plugins/admin/view/parameter_list')
    def admin_parameter_save(self):
        KMParameterAdmin.save_parameter(self.data)
        self.result['menu_list'] = get_menu_list()
        self.result['parameters'] = KMParameter.all()


    def admin_file_upload(self):
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


    def admin_file_remove(self):
        """
        Remove the file.
        """
        for remove_target in self.data.get_request().forms:
            target = remove_target.split(',')
            os.remove(DATA_DIR_PATH + os.sep + target[0] + os.sep + target[1])
            print("remove. " + DATA_DIR_PATH + os.sep + target[0] + os.sep + target[1])


    def admin_select_dir(self):
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
