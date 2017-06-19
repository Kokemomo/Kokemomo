#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.model.km_parameter_table import KMParameter

class KMParameterAdmin:

    @classmethod
    def save_parameter(cls, data):
        id = data.get_request_parameter("id")
        delete = data.get_request_parameter("delete", default=None)
        if delete is None:
            parameter = KMParameter.get(id)
            parameter.set_data(data)
            parameter.save()
        else:
            KMParameter.delete_by_id(id)

