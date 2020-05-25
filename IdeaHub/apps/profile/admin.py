from django.contrib import admin
from .models import Profile, VerificationCode

admin.site.register(Profile)
admin.site.register(VerificationCode)
