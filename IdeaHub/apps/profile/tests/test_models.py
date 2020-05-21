from django.test import TestCase
from IdeaHub.apps.profile.models import Profile, VerificationCode
from django.contrib.auth.models import User

USERNAME = 'test user'
EMAIL = 'testemail@gmail.com'
PASSWORD = 'test password'
VERIFICATION_CODE = '124'


class ProfileModelTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username=USERNAME,
            password=PASSWORD,
            email=EMAIL
        )
        Profile.objects.create(user=user)

    def test_profile_bound_to_user(self):
        profile = Profile.objects.get(
            user__username=USERNAME
        )
        self.assertEqual(profile.user.username, USERNAME)
        self.assertEqual(profile.user.email, EMAIL)

    def test_password_hashed(self):
        profile = Profile.objects.get(
            user__username=USERNAME
        )
        self.assertNotEqual(profile.user.password, PASSWORD)


class VerificationCodeModel(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username=USERNAME,
            password=PASSWORD,
            email=EMAIL
        )
        Profile.objects.create(user=user)
        VerificationCode.objects.create(
            code=VERIFICATION_CODE,
            user=user
        )

    def test_code_bound_to_user(self):
        code = VerificationCode.objects.get(user__email=EMAIL)
        self.assertEqual(code.user.username, USERNAME)
        self.assertEqual(code.code, VERIFICATION_CODE)
