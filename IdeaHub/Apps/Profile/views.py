from django.http import HttpResponse, request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..Profile.models import Profile


@api_view(['GET'])
def get_user_profiles(request):
    return Response({
        'name': 'Brian'
    })
