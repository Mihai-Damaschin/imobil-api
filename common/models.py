from django.db import models


class Media(models.Model):
    url = models.CharField(max_length=200)
    is_main_cover = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return {
            "url": self.url,
            "is_main_cover": self.is_main_cover
        }
