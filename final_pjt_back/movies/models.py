from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    rate_average = models.FloatField()
    poster_path = models.URLField(max_length=200)
    overview = models.TextField()
    release_date = models.DateField()
    # genres = models.ManyToManyField(Genre, verbose_name=_(""))

# class Genre(models.Model):

class WatchList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie, verbose_name='watchlist')
    cover_image = models.ImageField(blank=True)