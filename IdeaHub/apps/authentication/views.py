from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers.signup_serializer import SignUpSerializer
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import vcode
from ..profile.models import VerificationCode


@api_view(['POST'])
def sign_up(request):
    data = request.data
    serializer = SignUpSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    response = None

    try:
        User.objects.get(email=data.get('email'))
        user_exist_message = 'a user with this email address exist.'

        response = Response({
            'user': [user_exist_message]
        }, status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        if data.get('password') != data.get('confirm_password'):
            password_error = 'the passwords do not match'

            response = Response({
                'password': [password_error]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code = vcode.digits()
            success_message = 'a verification code has been sent to your email.'

            user = User.objects.create_user(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                email=data.get('email'),
                password=data.get('password'),
                username=data.get('email'),
                is_active=False
            )

            VerificationCode.objects.create(
                code=str(code),
                user=user
            )

            response = Response({
                'message': [success_message]
            }, status=status.HTTP_201_CREATED)

    return response
