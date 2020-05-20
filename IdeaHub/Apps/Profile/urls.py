from django.urls import path
from . import views

urlpatterns = [
    path('users', views.get_user_profiles, name='index')
]
