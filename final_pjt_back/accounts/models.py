from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Genre

# Create your models here.
class User(AbstractUser):
    # profile_img = models.URLField(blank=True, max_length=200)
    profile_img = models.ImageField(upload_to="image", blank=True, max_length=200)
    following = models.ManyToManyField('self', symmetrical=False, blank=True, related_name="followers")

    profile_message = models.CharField(blank=True, max_length=500)
    preferences = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return self.username