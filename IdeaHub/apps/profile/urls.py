from django.urls import path
from ..profile import views

urlpatterns = [
    path('profile', views.fetch_user_profile)
]
