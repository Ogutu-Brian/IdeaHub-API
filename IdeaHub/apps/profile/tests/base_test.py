from ...authentication.tests.base_test import BaseTest as AuthBaseTest


class BaseTest(AuthBaseTest):
    def fetch_user_profile(self):
        response = self.client.get(path=)
