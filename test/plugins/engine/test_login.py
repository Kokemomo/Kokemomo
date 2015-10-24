__author__ = 'hiroki-m'
import bcrypt
from unittest import TestCase
from kokemomo.plugins.engine.controller.km_login import KMLogin
from kokemomo.plugins.engine.model.km_user_table import KMUser
from kokemomo.settings import SETTINGS

TEST_PASSWORD = 'test_password'
TEST_SAVE_SESSION = 'save_session'
TEST_REMOVE_SESSION = 'remove_session'

class LoginTest(TestCase):

    @classmethod
    def setup_class(clazz):
        pass

    @classmethod
    def teardown_class(clazz):
        pass

    def setUp(self):
        self.login = TestLogin()

    def teardown(self):
        pass

    def test_login(self):
        req = TestRequest()
        result = self.login.auth(req, 'test', 'test_password')
        assert req.result == TEST_SAVE_SESSION
        assert result == TestLogin.RESULT_SUCCESS

    def test_logout(self):
        req = TestRequest()
        self.login.logout(req)
        assert req.result == TEST_REMOVE_SESSION



class TestLogin(KMLogin):

    @classmethod
    def get_user(cls, user_id):
        user = KMUser()
        user.password = bcrypt.hashpw(TEST_PASSWORD.encode(SETTINGS.CHARACTER_SET), bcrypt.gensalt())
        return user


    @classmethod
    def save_session(cls, request, id):
        request.result = TEST_SAVE_SESSION


    @classmethod
    def remove_session(cls, request):
        request.result = TEST_REMOVE_SESSION


class TestRequest():

    def __init__(self):
        self.result = ''

    def get_request(self):
        return self

