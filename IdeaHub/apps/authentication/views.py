from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers.serializer import(
    SignUpSerializer,
    VerifyUserSerializer,
    LoginSerializer
)
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import vcode
from ..profile.models import(
    VerificationCode,
    Profile
)
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from .utils.response_messages import ResponseMessages


@api_view(['POST'])
def sign_up(request):
    data = request.data
    serializer = SignUpSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    response = None
    code = vcode.digits()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    username = data.get('email')
    email_subject = 'IdeaHub Verification Code'
    email_message = 'Your verification code is {}'.format(code)
    ideahub_email = 'noreply@ideahub.com'
    confirm_password = data.get('confirm_password')

    user, created = User.objects.get_or_create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        username=email,
        is_active=False
    )

    if not created:
        response = Response({
            'user': [ResponseMessages.existing_user_error_message]
        }, status=status.HTTP_400_BAD_REQUEST)
    elif password != confirm_password:
        response = Response({
            'password': [ResponseMessages.unmatching_password_error]
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        VerificationCode.objects.create(
            code=str(code),
            user=user
        )

        send_mail(
            subject=email_subject,
            message=email_message,
            from_email=ideahub_email,
            recipient_list=[email],
            fail_silently=False
        )

        response = Response({
            'message': [ResponseMessages.success_signup_message]
        }, status=status.HTTP_201_CREATED)

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

            response = Response({
                'message': [ResponseMessages.successful_account_verification]
            }, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        response = Response({
            'user': [ResponseMessages.unexisting_user_error]
        }, status=status.HTTP_401_UNAUTHORIZED)

    return response


@api_view(['POST'])
def login(request):
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
            authenticateduser = authenticate(
                request=request,
                username=email,
                password=password
            )

            if not authenticateduser:
                response = Response({
                    'message': [ResponseMessages.invalid_password_error]
                }, status=status.HTTP_401_UNAUTHORIZED)
            else:
                pass
    except ObjectDoesNotExist:
        response = Response({
            'user': [ResponseMessages.unexisting_user_error]
        }, status=status.HTTP_401_UNAUTHORIZED)

    return response
