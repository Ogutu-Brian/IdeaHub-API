from rest_framework import serializers


class SignUpSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=250,)
    last_name = serializers.CharField(max_length=250)
    email = serializers.EmailField(max_length=250)
    password = serializers.CharField(max_length=250)
    confirm_password = serializers.CharField(max_length=250)
