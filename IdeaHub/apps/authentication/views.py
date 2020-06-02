from rest_framework.response import Response
from rest_framework.decorators import (api_view, permission_classes)
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.hashers import check_password
from rest_framework import status
from .serializers.serializer import(
    SignUpSerializer,
    VerifyUserSerializer,
    LoginSerializer,
    CodeResendSerializer
)
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from ..profile.models import(VerificationCode, Profile)
from .utils.response_messages import ResponseMessages
from .utils.helpers import send_verification_code
from rest_framework_simplejwt.tokens import (RefreshToken, OutstandingToken)
from rest_framework.permissions import IsAuthenticated
import datetime


@api_view(['POST'])
def sign_up(request):
    data = request.data
    serializer = SignUpSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    response = None
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    username = data.get('email')
    confirm_password = data.get('confirm_password')

    if password != confirm_password:
        response = Response({
            'password': [ResponseMessages.unmatching_password_error]
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'password': password,
                'username': username,
                'is_active': False
            }
        )

        if not user.is_active:
            user.set_password(password)
            user.save()
            response = send_verification_code(user=user, email=email)
        else:
            response = Response({
                'user': [ResponseMessages.existing_user_error_message]
            }, status=status.HTTP_400_BAD_REQUEST)

    return response


@api_view(['POST'])
def verify_user(request):
    response = None
    data = request.data
    serializer = VerifyUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        email = data.get('email')
        code = data.get('verification_code')
        user = User.objects.get(email=email)

        if not user.is_active:
            verification_code = VerificationCode.objects.get(
                user__email=email
            )

            if verification_code.code != code:
                response = Response({
                    'verification_code': [ResponseMessages.mismatching_verification_code]
                }, status=status.HTTP_400_BAD_REQUEST)
            else:
                user = verification_code.user
                user.is_active = True
                user.save()
                Profile.objects.create(user=user)
                verification_code = VerificationCode.objects.get(
                    user__email=user.email
                )
                verification_code.delete()
                refresh = RefreshToken.for_user(user=user)

                response = Response({
                    'message': [ResponseMessages.successful_account_verification],
                    'access': str(refresh.access_token),
                    'refresh': str(refresh)
                }, status=status.HTTP_200_OK)
        else:
            response = Response({
                'verification_code': [ResponseMessages.multiple_verification_error]
            }, status=status.HTTP_403_FORBIDDEN)
    except ObjectDoesNotExist:
        response = Response({
            'user': [ResponseMessages.unexisting_user_error]
        }, status=status.HTTP_401_UNAUTHORIZED)

    return response


@api_view(['POST'])
def login_user(request):
    response = None
    data = request.data
    serializer = LoginSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    email = data.get('email')
    password = data.get('password')

    try:
        user = User.objects.get(email=email)

        if not user.is_active:
            response = Response({
                'user': [ResponseMessages.unverified_account_error]
            }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            matching_password = check_password(
                password=password,
                encoded=user.password
            )

            if not matching_password:
                response = Response({
                    'message': [ResponseMessages.invalid_password_error]
                }, status=status.HTTP_401_UNAUTHORIZED)
            else:
                refresh = RefreshToken.for_user(user=user)
                response = Response({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh)
                }, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        response = Response({
            'user': [ResponseMessages.unexisting_user_error]
        }, status=status.HTTP_401_UNAUTHORIZED)

    return response


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    email = request.user
    response = None
    user = User.objects.get(email=email)
    outstandingTokens = OutstandingToken.objects.filter(user=user)

    if not len(outstandingTokens):
        response = Response({
            'message': [ResponseMessages.invalid_token]
        }, status=status.HTTP_401_UNAUTHORIZED)
    else:
        [token.delete() for token in outstandingTokens]

        response = Response({
            'message': [ResponseMessages.logout_message]
        }, status=status.HTTP_200_OK)

    return response


@api_view(['POST'])
def resend_verification_code(request):
    data = request.data
    serializer = CodeResendSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    email = data.get('email')

    try:
        user = User.objects.get(email=email)

        if not user.is_active:
            response = send_verification_code(
                user=user,
                email=email,
                response_status=status.HTTP_200_OK
            )
        else:
            response = Response({
                'verification_code': [
                    ResponseMessages.multiple_verification_error
                ]
            }, status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        response = Response({
            'user': [ResponseMessages.unexisting_user_error]
        }, status=status.HTTP_400_BAD_REQUEST)

    return response
