from django.test import TestCase
from IdeaHub.Apps.Profile.models import Profile
from django.contrib.auth.models import User

class ProfileModelTests(TestCase):
    USERNAME = 'test user'
    EMAIL = 'test email'
    PASSWORD = 'test password'

    def setUp(self):
        user = User.objects.create_user(
            username=ProfileModelTests.USERNAME,
            password=ProfileModelTests.PASSWORD,
            email=ProfileModelTests.EMAIL
        )
        Profile.objects.create(user=user)

    def test_profile_bound_to_user(self):
        profile = Profile.objects.get(
            user__username=ProfileModelTests.USERNAME
        )
        self.assertEqual(profile.user.username, ProfileModelTests.USERNAME)
        self.assertEqual(profile.user.email, ProfileModelTests.EMAIL)

    def test_password_hashed(self):
        profile = Profile.objects.get(
            user__username=ProfileModelTests.USERNAME
        )
        self.assertNotEqual(profile.user.password, ProfileModelTests.PASSWORD)
