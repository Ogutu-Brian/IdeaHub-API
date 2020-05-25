from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models

from .abstract_models import TimeStampedModel


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, **fields):
        return None

class User(AbstractBaseUser, TimeStampedModel, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True)

    objects = UserManager()

    class Meta:
        verbose_name_plural = "All Users"

    def __str__(self):
        """Returns a string representation of the user"""
        return self.email
