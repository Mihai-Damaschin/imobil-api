from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser, PermissionsMixin

from .constants import UserTypes


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("email address", unique=True, max_length=100, blank=True)
    full_name = models.CharField("full name", max_length=100, blank=True)
    type = models.CharField("user type", default=UserTypes.REGULAR, max_length=30)
    photo = models.CharField("user photo", default="", max_length=150)
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = models.BooleanField(
        "active",
        default=True,
    )
    date_joined = models.DateTimeField("date joined", default=timezone.now)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return {
            "full_name": self.full_name,
            "email": self.email,
            "type": self.type
        }

    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False
