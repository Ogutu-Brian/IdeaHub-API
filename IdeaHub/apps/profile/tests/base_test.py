from .test_data import FETCH_PROFILE_ENDPOINT, ResponseData
from ...authentication.tests.base_test import BaseTest as AuthBaseTest


class BaseTest(AuthBaseTest):
    response_data = ResponseData

    def authenticate_user(self):
        self.sign_up()
        self.verify_user()
        self.login()

    def fetch_user_profile(self):
        response = self.client.get(path=FETCH_PROFILE_ENDPOINT)

        return response
