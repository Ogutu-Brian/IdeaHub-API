from .base_test import BaseTest
from .test_data import (
    password,
    email,
    LOGIN_ENDPOINT
)
from rest_framework import status


class TestLogin(BaseTest):
    def tearDown(self):
        self.clear_all_users()
        super().tearDown()

    def test_missing_field(self):
        response = self.client.post(
            path=LOGIN_ENDPOINT,
            data={
                'password': password
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.data,
            self.response_data.missing_email_field_error
        )

    def test_invalid_email_field(self):
        response = self.client.post(
            path=LOGIN_ENDPOINT,
            data=self.test_data.invalid_email_details,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.data,
            self.response_data.invalid_email_error
        )

    def test_user_does_not_exist(self):
        response = self.login()

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

        self.assertEqual(
            response.data,
            self.response_data.user_does_not_exist_error
        )

    def test_unverified_user(self):
        self.sign_up()
        response = self.login()

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

        self.assertEqual(
            response.data,
            self.response_data.unverified_user_error
        )

    def test_invalid_password(self):
        self.sign_up()
        self.verify_user()
        response = self.login()

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

        self.assertEqual(
            response.data,
            self.response_data.invalid_password_error
        )
