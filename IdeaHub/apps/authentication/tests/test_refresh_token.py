from .base_test import BaseTest
from .test_data import REFRESH_TOKEN_ENDPOINT
from rest_framework import status


class TestRefreshToken(BaseTest):
    def tearDown(self):
        super().tearDown()
        self.clear_all_users()

    def test_refresh_token_generation(self):
        self.sign_up()
        self.verify_user()
        login_response = self.login()
        refresh_token = login_response.data.get('refresh')

        response = self.client.post(
            path=REFRESH_TOKEN_ENDPOINT,
            data={
                'refresh': refresh_token
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            'access' in response.data.keys(),
            True
        )
