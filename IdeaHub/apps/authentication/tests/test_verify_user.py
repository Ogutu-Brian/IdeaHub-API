from rest_framework import status
from .test_data import (
    VERIFICATION_ENDPOINT,
    email,
    unexisting_email,
    invalid_code
)
from .base_test import BaseTest
from django.contrib.auth.models import User
from ...profile.models import (
    Profile,
    VerificationCode
)


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

    def test_unexisting_user(self):
        response = self.client.post(
            path=VERIFICATION_ENDPOINT,
            data={
                'email': unexisting_email,
                'verification_code': self.verification_code
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

        self.assertEqual(
            response.data,
            self.response_data.user_does_not_exist_error
        )

    def test_mismatching_codes(self):
        response = self.client.post(
            path=VERIFICATION_ENDPOINT,
            data={
                'email': email,
                'verification_code': invalid_code
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

    def test_activating_user(self):
        response = self.post_verification_code()
        user = User.objects.get(email=email)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(user.is_active, True)

        self.assertEqual(
            response.data,
            self.response_data.verify_user_response
        )

    def test_creating_user_profile(self):
        self.post_verification_code()

        profile = Profile.objects.get(user__email=email)

        self.assertEqual(profile.user.email, email)

    def test_delete_verification_code(self):
        self.post_verification_code()
        verification_codes = VerificationCode.objects.all()

        self.assertEqual(len(verification_codes), 0)
