from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)

    referral_code = models.CharField(max_length=15, null=True, blank=True)
