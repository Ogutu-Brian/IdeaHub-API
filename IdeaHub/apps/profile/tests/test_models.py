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

    def get_profile(self):
        profile = Profile.objects.get(
            user__username=USERNAME
        )

        return profile

    def test_profile_bound_to_user(self):
        profile = self.get_profile()

        self.assertEqual(profile.user.username, USERNAME)
        self.assertEqual(profile.user.email, EMAIL)

    def test_password_hashed(self):
        profile = self.get_profile()

        self.assertNotEqual(profile.user.password, PASSWORD)

    def test_model_representation(self):
        profile = self.get_profile()
        representation_string = '{} {}'.format(
            profile.user.first_name,
            profile.user.last_name
        )

        self.assertEqual(profile.__str__(), representation_string)


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

    def get_verification_code(self):
        code = VerificationCode.objects.get(user__email=EMAIL)

        return code

    def test_code_bound_to_user(self):
        code = self.get_verification_code()

        self.assertEqual(code.user.username, USERNAME)
        self.assertEqual(code.code, VERIFICATION_CODE)

    def test_model_representation(self):
        code = self.get_verification_code()

        self.assertEqual(code.__str__(), code.code)
