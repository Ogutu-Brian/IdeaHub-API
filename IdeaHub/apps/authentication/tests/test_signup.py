from .test_data import (
    SIGN_UP_ENDPOINT,
    email
)
from rest_framework import status
from ...profile.models import VerificationCode
from .base_test import BaseTest
from django.contrib.auth.models import User


class TestUserSignUp(BaseTest):
    def tearDown(self):
        super().tearDown()
        self.clear_all_users()

    def test_missing_field(self):
        response = self.client.post(
            path=SIGN_UP_ENDPOINT,
            data=self.test_data.incomplete_details,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.data,
            self.response_data.incomplete_details_error
        )

    def test_invalid_email_field(self):
        response = self.client.post(
            path=SIGN_UP_ENDPOINT,
            data=self.test_data.invalid_email_details,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.data,
            self.response_data.ivalid_email_error,
        )

    def test_sign_up_more_than_once(self):
        self.sign_up()
        response = self.sign_up()

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.data,
            self.response_data.user_exist_error
        )

    def test_successful_sign_up(self):
        response = self.sign_up()

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.data,
            self.response_data.success_response
        )

    def test_password_mismatch(self):
        response = self.client.post(
            path=SIGN_UP_ENDPOINT,
            data=self.test_data.mismatching_password_data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.data,
            self.response_data.mismatching_password_error
        )

    def test_successful_saving_of_verification_code(self):
        response = self.sign_up()
        code = self.get_verification_code()
        verification_codes = VerificationCode.objects.all()

        self.assertEqual(len(verification_codes), 1)
        self.assertEqual(verification_codes[0].code, code.code)

    def test_successful_saving_user(self):
        self.sign_up()
        user = User.objects.get(email=email)

        self.assertEqual(user.is_active, False)
