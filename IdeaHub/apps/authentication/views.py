from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers.signup_serializer import SignUpSerializer


@api_view(['POST'])
def sign_up(request):
    data = request.data
    serializer = SignUpSerializer(data=data)
    serializer.is_valid(raise_exception=True)
