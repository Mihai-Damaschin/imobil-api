from django.db import models

from django.contrib.auth import get_user_model
from estates.models import Estate

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    active_till = models.DateTimeField()

    def __str__(self):
        return {
            "author": self.author,
            "estate": self.estate,
            "is_active": self.is_active,
            "active_till": self.active_till
        }
