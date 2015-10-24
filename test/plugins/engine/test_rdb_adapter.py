# -*- coding: utf-8 -*-
import unittest

from sqlalchemy.exc import SQLAlchemyError

from kokemomo.plugins.engine.model.km_storage import initialize
from kokemomo.plugins.engine.model.km_storage.impl.km_rdb_adapter import adapter, Transaction, rollback

# TODO: ErrorもRDBAdapter内に実装する


class User(adapter.Model):
    name = adapter.Column(adapter.String(50))

    def validate(self):
        self.name = self.name.lower() # for test

class SimpleTestCase(unittest.TestCase):
    def setUp(self):
        initialize(rdb_path='sqlite:///:memory:')
        self.user = User(name='kokemomo')
        self.user.save()

    def tearDown(self):
        pass

    def test_get(self):
        user = User.get(id=self.user.id)
        self.assertEqual('kokemomo', user.name)

    def test_find(self):
        user = User.find(name='kokemomo')[0]
        self.assertEqual('kokemomo', user.name)

    def test_delete(self):
        User.delete(id=self.user.id)
        self.assertEqual(0, len(User.all()))

    def test_rollback(self):
        self.user.name = 'steve'
        self.assertEqual('steve', self.user.name)
        rollback()
        self.assertEqual('kokemomo', self.user.name)

    def test_transaction(self):
        with Transaction.begin():
            john = User(name='jonh')
            steve = User(name='steve')
            Transaction.add(john)
            Transaction.add(steve)
        self.assertEqual(3, len(User.all()))

    def test_failed_transaction(self):
        def trans():
            try:
                with Transaction.begin():
                    john = User(id=999,name='jonh')
                    steve = User(id=999,name='steve')
                    Transaction.add(john)
                    Transaction.add(steve)
            except SQLAlchemyError:
                Transaction.rollback()
                raise
        self.assertRaises(Exception, trans)
        self.assertEqual(1, len(User.all()))

        # トランザクションが失敗した後にも操作を行えるか
        john = User(id=999,name='jonh')
        john.save()
        self.assertEqual(2, len(User.all()))

    def test_validation(self):
        steve = User(name='STEVE')
        steve.save()
        self.assertEqual('steve', steve.name)

    def test_no_validation(self):
        steve = User(name='STEVE')
        steve.save(validate=False)
        self.assertNotEqual('steve', steve.name)
