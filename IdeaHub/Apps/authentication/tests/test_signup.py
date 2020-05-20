from rest_framework.test import APIClient
from django.test import TestCase
from .test_data import SignUpData
from rest_framework import status


class TestUserLogIn(TestCase):
    client = APIClient()

    def test_missing_field(self):
        response = self.client.post(
            '/authentication/sign-up',
            SignUpData.TestData.incomplete_details,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_406_NOT_ACCEPTABLE
        )

        self.assertEqual(
            response.data,
            SignUpData.ResponseData.incomplete_details_error
        )
