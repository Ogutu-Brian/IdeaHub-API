from rest_framework import status
from .test_data import (
    VERIFICATION_ENDPOINT,
    email
)
from .base_test import BaseTest


class VerifyUserTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.sign_up()
        self.verification_code = self.get_verification_code()

    def tearDown(self):
        super().tearDown()
        self.clear_all_users()

    def post_verification_code(self):
        response = self.client.post(
            path=VERIFICATION_ENDPOINT,
            data={
                'verification_code': self.verification_code,
                'email': email
            },
            format='json'
        )

        return response

    def test_missing_field(self):
        response = self.client.post(
            path=VERIFICATION_ENDPOINT,
            data={'verification_code': self.verification_code},
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.data,
            self.response_data.missing_verification_field_error
        )

    def test_invalid_email(self):
        response = self.client.post(
            path=VERIFICATION_ENDPOINT,
            data={
                'verification_code': self.verification_code,
                'email': 'invalidemail'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.data,
            self.response_data.ivalid_email_error
        )

    def test_mismatching_codes(self):
        response = self.client.post(
            path=VERIFICATION_ENDPOINT,
            data={
                'email': email,
                'verification_code': 'invalid code'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.data,
            self.response_data.mismatching_verification_code_error
        )
