from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    password = models.CharField(
        max_length=128, verbose_name='password', blank=False)
    email = models.EmailField(
        blank=False, max_length=254, verbose_name='email address')
