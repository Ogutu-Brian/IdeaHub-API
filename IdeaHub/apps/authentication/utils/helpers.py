from ...profile.models import VerificationCode
from rest_framework import status
from rest_framework.response import Response
import vcode
from django.core.mail import send_mail
from .response_messages import ResponseMessages


def send_verification_code(user, email, response_status=status.HTTP_201_CREATED):
    code = vcode.digits()
    email_subject = 'IdeaHub Verification Code'
    ideahub_email = 'noreply@ideahub.com'

    verification_code, created = VerificationCode.objects.get_or_create(
        user=user,
        defaults={'code': str(code)}
    )

    email_message = 'Your verification code is {}'.format(
        verification_code.code
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
    }, status=response_status)

    return response
