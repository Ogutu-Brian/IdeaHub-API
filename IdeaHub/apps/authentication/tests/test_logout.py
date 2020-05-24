from .base_test import BaseTest
from .test_data import LOGIN_ENDPOINT
from rest_framework import status


class TestLogout(BaseTest):
    def setUp(self):
        self.sign_up()
        self.verify_user()
        super().setUp()

    def tearDown(self):
        super().tearDown()
        self.clear_all_users()

    def test_logout_with_invalid_token(self):
        response = self.logout()

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

        self.assertEqual(
            response.data,
            self.response_data.no_credentials_error
        )

    def test_multiple_logout(self):
        self.login()
        self.logout()
        response = self.logout()

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

        self.assertEqual(
            response.data,
            self.response_data.invalid_token_error
        )

    def test_successful_logout(self):
        self.login()
        response = self.logout()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data,
            self.response_data.successful_logout
        )
