from django.db import models
from django.utils import timezone

from django.contrib.auth import get_user_model

from common.models import Media

User = get_user_model()


class Estate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, default="")
    housing_fund = models.CharField(max_length=50)
    rooms_count = models.IntegerField()
    floor = models.IntegerField()
    max_floor = models.IntegerField()
    total_area = models.DecimalField(decimal_places=2, max_digits=10)
    state = models.CharField(max_length=50)
    balcony = models.BooleanField()
    parking_space = models.CharField(max_length=50)
    description = models.CharField(max_length=3000, default="")
    media = models.ManyToManyField(Media)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return {
            "user": self.user,
            "total_area": self.total_area
        }
