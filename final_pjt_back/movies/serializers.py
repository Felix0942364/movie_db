from rest_framework import serializers
from .models import Movie, WatchList

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title', 'overview', 'rate_average',)
        # fields = ('id', 'title', 'content')


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'
        read_only_fields = ('user',)
