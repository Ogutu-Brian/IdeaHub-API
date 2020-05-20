from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers.signup_serializer import SignUpSerializer


@api_view(['POST'])
def sign_up(request):
    data = request.data
    serializer = SignUpSerializer(data=data)
    response = None

    if(serializer.is_valid()):
        pass
    else:
        response = Response(
            serializer.errors,
            status=status.HTTP_406_NOT_ACCEPTABLE
        )

    return response
