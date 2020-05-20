from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['POST'])
def sign_up(request):
    return Response({
        'test': 'test'
    }, status=status.HTTP_201_CREATED)
