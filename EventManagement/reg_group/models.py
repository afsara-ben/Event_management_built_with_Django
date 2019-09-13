from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe


class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_agency = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    email = models.EmailField(max_length=255, default=None, blank=True, null=True)


class User_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

