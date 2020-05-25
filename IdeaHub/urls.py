from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from .utils.routing import get_app_routes
from IdeaHub.apps import authentication

admin.site.site_header = 'IdeaHub'
admin.site.index_title = 'IdeaHub Administration'

urlpatterns = [
    path('authentication/', include(
        get_app_routes(authentication.APP_NAME)
    )),
    path('admin/', admin.site.urls)
]
