from .test_data import FETCH_PROFILE_ENDPOINT, ResponseData
from rest_framework.test import APIClient, APITestCase


class BaseTest(APITestCase):
    client = APIClient()
    response_data = ResponseData

    def authenticate_user(self):
        self.client.force_authenticate()

    def fetch_user_profile(self):
        response = self.client.get(path=FETCH_PROFILE_ENDPOINT)

        return response
