from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150, blank=True,)
    user_1 = models.TextField(null=True, blank=True,)
    timeframe = models.TimeField(null=True, blank=True,)
    uid_home = models.ForeignKey(
        "home.HomePage",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customtext_uid_home",
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()
    uid_home = models.UUIDField(null=True, blank=True,)

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
