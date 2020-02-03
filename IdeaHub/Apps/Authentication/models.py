from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from django_extensions.db.models import TimeStampedModel


class User(AbstractBaseUser, TimeStampedModel):
    email = models.EmailField(db_index=True, unique=True)

class Meta:
    verbose_name_plural = "All Users"

def __str__(self):
    """Returns a string representation of the user"""
    return self.email