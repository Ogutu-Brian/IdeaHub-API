from django.conf.urls import include
from django.urls import path
from .utils.routing import get_app_routes

urlpatterns = [
    path('profile/', include(get_app_routes('profile'))),
    path('authentication/', include(get_app_routes('authentication')))
]
