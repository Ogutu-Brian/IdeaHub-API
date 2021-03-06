from rest_framework.test import APIClient
from ...profile.models import VerificationCode
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.test import TestCase
from .test_data import (
    SignUpData,
    SIGN_UP_ENDPOINT,
    VERIFICATION_ENDPOINT,
    LOGIN_ENDPOINT,
    LOGOUT_ENDPOINT,
    CODE_RESEND_ENDPOINT,
    email
)


class BaseTest(APITestCase):
    client = APIClient()
    response_data = SignUpData.ResponseData
    test_data = SignUpData.TestData

    def sign_up(self):
        response = self.client.post(
            path=SIGN_UP_ENDPOINT,
            data=self.test_data.complete_details,
            format='json'
        )

        return response

    def clear_all_users(self):
        users = User.objects.all()
        [user.delete() for user in users]

    def clear_all_verification_codes(self):
        Verification_codes = VerificationCode.objects.all()
        [verification_code.delete() for verification_code in Verification_codes]

    def get_verification_code(self):
        code = VerificationCode.objects.get(
            user__email=email
        )

        return code.code

    def verify_user(self):
        verification_code = self.get_verification_code()

        response = self.client.post(
            path=VERIFICATION_ENDPOINT,
            data={
                'verification_code': verification_code,
                'email': email
            }
        )

        return response

    def login(self):
        response = self.client.post(
            path=LOGIN_ENDPOINT,
            data=self.test_data.complete_details,
            format='json'
        )

        access_token = response.data.get('access')
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(access_token)
        )

        return response

    def logout(self):
        response = self.client.post(
            path=LOGOUT_ENDPOINT,
            data=self.test_data.complete_details,
            format='json'
        )

        return response

    def resend_verification_code(self):
        response = self.client.post(
            path=CODE_RESEND_ENDPOINT,
            data=self.test_data.complete_details,
            format='json'
        )

        return response
