from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    twitter_token = models.CharField(max_length=255, blank=True)
    facebook_token = models.CharField(max_length=255, blank=True)