from rest_framework.test import APIClient
from django.test import TestCase
from .test_data import SignUpData, SIGN_UP_ENDPOINT
from rest_framework import status
from django.contrib.auth.models import User


class TestUserLogIn(TestCase):
    client = APIClient()

    def sign_up(self):
        response = self.client.post(
            SIGN_UP_ENDPOINT,
            SignUpData.TestData.complete_details
        )

        return response

    def test_missing_field(self):
        response = self.client.post(
            SIGN_UP_ENDPOINT,
            SignUpData.TestData.incomplete_details,
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
            SIGN_UP_ENDPOINT,
            SignUpData.TestData.invalid_email_details,
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
