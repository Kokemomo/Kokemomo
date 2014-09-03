#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'hiroki'

from kokemomo.plugins.recommend.model.km_history_table import get_session, find, find_list, update
from kokemomo.plugins.recommend.controller.km_recommend import get_recommend, create_user_record, jaccard

"""
Test class km_reccomend.

"""

class TestRecommend:

    @classmethod
    def setup_class(clazz):
        pass

    @classmethod
    def teardown_class(clazz):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_recommend(self):
        session = get_session()
        update("0001", "user01", "AAA", 1, session)
        update("0002", "user01", "BBB", 1, session)
        update("0003", "user01", "CCC", 1, session)
        update("0004", "user02", "AAA", 1, session)
        update("0005", "user03", "BBB", 1, session)
        column = ["AAA", "BBB", "CCC"]
        user_similarity = get_recommend("user02", column)
        assert user_similarity['user01'] > user_similarity['user03']
        session.close()
