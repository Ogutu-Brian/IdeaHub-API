from django.conf.urls import include
from django.urls import path
from django.contrib.auth.models import User
from django.contrib import admin
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('admin', admin.site.urls),
    path('', include(router.urls)),
    path('example_users/', include('IdeaHub.Apps.Profile.urls')),
]
