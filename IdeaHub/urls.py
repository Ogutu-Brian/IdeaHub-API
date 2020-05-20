from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('profile/', include('IdeaHub.apps.profile.urls')),
]
