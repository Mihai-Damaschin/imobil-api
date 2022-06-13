from django.db import models

from django.contrib.auth import get_user_model
from estates.models import Estate

User = get_user_model()


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return {
            'user': self.user,
            'estate': self.estate,
            'is_active': self.is_active
        }
