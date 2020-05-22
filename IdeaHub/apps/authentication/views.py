from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers.serializer import(
    SignUpSerializer,
    VerifyUserSerializer
)
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import vcode
from ..profile.models import(
    VerificationCode,
    Profile
)
from django.core.mail import send_mail


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
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            password = data.get('password')
            username = data.get('email')
            email_subject = 'IdeaHub Verification Code'
            email_message = 'Your verification code is {}'.format(code)
            ideahub_email = 'noreply@ideahub.com'

            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                username=email,
                is_active=False
            )

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
                'message': [success_message]
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

        if(verification_code.code != code):
            response_message = 'The verification code does not match.'

            response = Response({
                'verification_code': [response_message]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            response_message = 'User account has successfully been activated.'
            user = verification_code.user
            user.is_active = True
            user.save()
            Profile.objects.create(user=user)
            verification_code = VerificationCode.objects.get(
                user__email=user.email
            )
            verification_code.delete()

            response = Response({
                'message': [response_message]
            }, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        response_message = 'A user with this email address does not exist.'

        response = Response({
            'user': [response_message]
        }, status=status.HTTP_401_UNAUTHORIZED)

    return response
