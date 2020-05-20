from django.urls import path
from ..profile import views

urlpatterns = [
    path('users', views.get_user_profiles)
]
