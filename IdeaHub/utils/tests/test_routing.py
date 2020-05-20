from unittest import TestCase
from ..routing import get_app_routes, APP_INITIAL


class RoutingTests(TestCase):
    def test_return_of_proper_route(self):
        self.assertEqual(
            get_app_routes('profile'),
            '{}.{}.urls'.format(APP_INITIAL, 'profile')
        )
