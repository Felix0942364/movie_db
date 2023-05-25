from django.db import models
from django.conf import settings


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Disclosure(models.Model):
    name = models.CharField(max_length=100)
    # 공개 비공개만 처리
    def __str__(self):
        return self.name


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    rate_average = models.FloatField()
    poster_path = models.URLField(max_length=200)
    overview = models.TextField()
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre, related_name="movies")


class WatchList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='watchlists' , on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(blank=True)
    scope_of_disclosure = models.ForeignKey(Disclosure, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie, blank=True)