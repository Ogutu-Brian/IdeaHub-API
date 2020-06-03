from .base_test import BaseTest
from rest_framework import status


class TestFetchUserProfile(BaseTest):
    def test_fetching_profile_before_logging_in(self):
        response = self.fetch_user_profile()

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

        self.assertEqual(
            response.data,
            self.response_data.no_credentials_error
        )

    def test_fetch_profile_successfully(self):
        self.authenticate_user()
        response = self.fetch_user_profile()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data,
            self.response_data.fetch_profile
        )
