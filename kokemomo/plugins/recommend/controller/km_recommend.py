#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'hiroki'

import sys

from kokemomo.plugins.recommend.model.km_history_table import find, find_list, update
from kokemomo.plugins.engine.controller.km_db_manager import *
from kokemomo.plugins.engine.utils.config import get_character_set_setting

"""
Reccomend class for Kokemomo CMS.
Adopt a user-based collaborative filtering.

[Design information]
--Table Column--
id, user_id, contents, count

--Data example--
0001, user01, AAA, 1
0002, user01, BBB, 1
0003, user01, CCC, 1
0004, user02, AAA, 1
0005, user03, BBB, 1

--Data example[After shaping]--
      |AAA|BBB|CCC|
user01|  1|  1|  1|
user02|  1|   |   |
user03|   |  1|   |

[Example]
If the target is user02.

--Code--
column = ["AAA", "BBB", "CCC"]
user_similarity = get_reccomend("user02", column)

--Result--
'user01': 0.3333333333333333
'user02': 1.0
'user03': 0.0

user01 is similar!

"""

db_manager = KMDBManager("engine")
charset = get_character_set_setting()

def get_recommend(user_id, columns, session):
    """
    Based on the history list, get the recommended level for the given user.

    :param user_id: target user_id
    :param columns: columns
    :return:recommend dictionary
    """
    history_list = find_list(10, session) # TODO: 期限を設定ファイルに抜き出し
    # Generate a user record that becomes a condition.
    user_record = create_user_record(user_id, history_list, columns)
    # Comparison with history.
    check_list = {}
    for history in history_list:
        if history.user_id is not user_id and not history.user_id in check_list:
            check_list[history.user_id] = create_user_record(history.user_id, history_list, columns)
    # Check similarity.
    result = {}
    for target in check_list:
        target = target.encode(charset)
        similarity = jaccard(user_record, check_list[target])
        result[target]=similarity
    return result

def create_user_record(user_id, history_list, columns):
    """
    Based on the item and the history list, you generate a record of the specified user.

    :param user_id: user id
    :param history_list: history list
    :param columns: columns
    :return: user record
    """
    record = []
    for i, column in enumerate(columns):
        record.append(0)
        for history in history_list:
            history_user = history.user_id.encode(charset)
            history_column =  history.contents.encode(charset)
            if user_id == history_user and column == history_column:
                record[i] = 1
                break
    return record

def jaccard(dic_x, dic_y):
    """
    Using jaccard coefficient, to determine the similarity.

    :param dic_x: matrix
    :param dic_y: matrix
    :return: similarity
    """
    product_set = 0.
    union = 0.
    for i in xrange(len(dic_x)):
        if dic_x[i] == 1 or dic_y[i] == 1:
            union += 1
            if dic_x[i] == 1 and dic_y[i] == 1:
                product_set += 1
    try:
        return product_set / union
    except ZeroDivisionError:
        return 0.0
