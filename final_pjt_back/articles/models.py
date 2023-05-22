from django.db import models
from django.conf import settings
# from movies.models import WatchList

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    liking_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='liked_articles')

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # watchlist = models.ManyToManyField(WatchList, verbose_name="article", blank=True)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments", on_delete=models.CASCADE)
    
    liking_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="liked_comments")
    
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
