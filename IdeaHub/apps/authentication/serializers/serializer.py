from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=250)
    password = serializers.CharField(max_length=250)


class SignUpSerializer(LoginSerializer):
    first_name = serializers.CharField(max_length=250,)
    last_name = serializers.CharField(max_length=250)
    confirm_password = serializers.CharField(max_length=250)


class VerifyUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=250)
    verification_code = serializers.CharField(max_length=250)


class CodeResendSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=250)
