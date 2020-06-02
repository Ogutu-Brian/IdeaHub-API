from .base_test import BaseTest
from django.contrib.auth.models import User
from rest_framework import status
from .test_data import CODE_RESEND_ENDPOINT
from ...profile.models import VerificationCode


class TestCodeResend(BaseTest):
    def setUp(self):
        super().setUp()
        self.sign_up()

    def tearDown(self):
        self.clear_all_users()
        super().tearDown()

    def test_invalid_email(self):
        response = self.client.post(
            path=CODE_RESEND_ENDPOINT,
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

    def test_missing_email_field(self):
        self.sign_up()
        response = self.client.post(
            path=CODE_RESEND_ENDPOINT,
            data={},
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

    def test_user_does_not_exist(self):
        self.clear_all_users()
        response = self.resend_verification_code()

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.data,
            self.response_data.user_does_not_exist_error
        )

    def test_already_activated_user(self):
        self.verify_user()
        response = self.resend_verification_code()

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.data,
            self.response_data.multiple_verification_error
        )

    def test_existing_verification_code(self):
        self.clear_all_verification_codes()
        response = self.resend_verification_code()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data,
            self.response_data.success_signup_response
        )

        self.assertEqual(
            len(VerificationCode.objects.all()),
            1
        )

    def test_successful_email_sending(self):
        response = self.resend_verification_code()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data,
            self.response_data.success_signup_response
        )

        self.assertEqual(
            len(VerificationCode.objects.all()),
            1
        )
