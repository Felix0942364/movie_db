from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Genre

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=150)
    profile_img = models.URLField(blank=True, max_length=200)
    followers = models.ManyToManyField('self', blank=True, related_name="following")

    preferences = models.ManyToManyField(Genre, blank=True)