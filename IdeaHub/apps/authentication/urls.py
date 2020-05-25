from django.urls import path
from ..authentication import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('sign-up', views.sign_up),
    path('verify', views.verify_user),
    path('login', views.login_user),
    path('logout', views.logout_user),
    path('refresh_token', TokenRefreshView.as_view())
]
