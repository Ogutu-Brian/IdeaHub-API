from django.urls import path
from ..authentication import views

urlpatterns = [
    path('sign-up', views.sign_up),
    path('verify', views.verify_user),
    path('login', views.login)
]
