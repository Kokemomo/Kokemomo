#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.model.km_user_table import KMUser
from kokemomo.plugins.engine.model.km_group_table import KMGroup
from kokemomo.plugins.engine.model.km_role_table import KMRole

class KMUserAdmin:

    @classmethod
    def save_user(cls, data):
        id = data.get_request_parameter("id")
        delete = data.get_request_parameter("delete", default=None)
        if delete is None:
            user = KMUser.get(id)
            user.set_data(data)
            user.save()
        else:
            KMUser.delete_by_id(id)

    @classmethod
    def save_group(cls, data):
        id = data.get_request_parameter("id")
        delete = data.get_request_parameter("delete", default=None)
        if delete is None:
            group = KMGroup.get(id)
            group.set_data(data)
            group.save()
        else:
            KMGroup.delete_by_id(id)

    @classmethod
    def save_role(cls, data):
        id = data.get_request_parameter("id")
        delete = data.get_request_parameter("delete", default=None)
        if delete is None:
            role = KMRole.get(id)
            role.set_data(data)
            role.save()
        else:
            KMRole.delete_by_id(id)

