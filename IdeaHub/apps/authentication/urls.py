from django.urls import path
from ..authentication import views

urlpatterns = [
    path('sign-up', views.sign_up)
]
