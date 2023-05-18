from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_img = models.URLField('프로필 이미지 URL', max_length=200)
    nickname = models.CharField(max_length=150)
    followers = models.ManyToManyField('self', verbose_name="following")