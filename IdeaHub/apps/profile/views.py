from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_user_profile(request):
    user = User.objects.get(email=request.user)

    return Response({
        'user': {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }
    }, status=status.HTTP_200_OK)
