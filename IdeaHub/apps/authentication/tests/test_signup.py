from rest_framework.test import APIClient
from django.test import TestCase
from .test_data import SignUpData, SIGN_UP_ENDPOINT
from rest_framework import status
from django.contrib.auth.models import User
from ...profile.models import VerificationCode


class TestUserLogIn(TestCase):
    client = APIClient()

    def tearDown(self):
        users = User.objects.all()
        [user.delete() for user in users]

    def sign_up(self):
        response = self.client.post(
            path=SIGN_UP_ENDPOINT,
            data=SignUpData.TestData.complete_details,
            format='json'
        )

        return response

    def test_missing_field(self):
        response = self.client.post(
            path=SIGN_UP_ENDPOINT,
            data=SignUpData.TestData.incomplete_details,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.data,
            SignUpData.ResponseData.incomplete_details_error
        )

    def test_invalid_email_field(self):
        response = self.client.post(
            path=SIGN_UP_ENDPOINT,
            data=SignUpData.TestData.invalid_email_details,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.data,
            SignUpData.ResponseData.ivalid_email_error,
        )

    def test_signup_more_than_once(self):
        self.sign_up()
        response = self.sign_up()

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.data,
            SignUpData.ResponseData.user_exist_error
        )

    def test_successful_sign_up(self):
        response = self.sign_up()

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.data,
            SignUpData.ResponseData.success_response
        )

    def test_password_mismatch(self):
        response = self.client.post(
            path=SIGN_UP_ENDPOINT,
            data=SignUpData.TestData.mismatching_password_data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.data,
            SignUpData.ResponseData.mismatching_password_error
        )

    def test_successful_saving_of_verification_code(self):
        response = self.sign_up()
        code = VerificationCode.objects.get(
            user__email=SignUpData.TestData.complete_details.get('email')
        )
        verification_codes = VerificationCode.objects.all()

        self.assertEqual(len(verification_codes), 1)
        self.assertEqual(verification_codes[0].code, code.code)
