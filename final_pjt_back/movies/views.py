from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, WatchListSerializer, GenreSerializer, MovieDetailSerializer
from .models import Movie, WatchList, Genre

import json
# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movies(request):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk = request.data.movie.pk)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MovieDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    # elif request.method == 'POST':
    #     serializer = MovieListSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         # serializer.save()
    #         serializer.save(user=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def get_details(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def watchlists(request):
    if request.method == 'GET':
        watchlists = get_list_or_404(WatchList, user=request.user)
        serializer = WatchListSerializer(watchlists, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    # elif request.method == 'PUT':
    #     serializer = WatchListSerializer(watchlists, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)

    # elif request.method == 'DELETE':
    #     watchlists.delete()
    #     return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def watchlist(request, watchlist_pk):
    if request.method == 'GET':
        watchlist = get_object_or_404(WatchList, pk = watchlist_pk)
        serializer = WatchListSerializer(watchlist)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        watchlist = get_object_or_404(WatchList, pk = watchlist_pk)
        if not Movie.objects.filter(pk=request.data.movie.pk).exists():
            serialized = MovieDetailSerializer(data=request.data)
            if serialized.is_valid(raise_exception=True):
                serialized.save()
        
        movie = Movie.objects.filter(pk=request.data.movie.pk)
        watchlist.movies.add(movie)
        serializer = WatchListSerializer(watchlist)
        return Response(serializer.data)


        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(watchlist=watchlist)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    elif request.method == 'PUT':
        serializer = WatchListSerializer(watchlist, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def MountedArticle(request, pk):
#     if request.method == 'GET':
#         pass

#     elif request.method == 'POST':
#         pass



@api_view(['GET'])
def genres(request):
    
    pass