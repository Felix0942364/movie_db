from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, WatchListSerializer
from .models import Movie, WatchList
# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movies(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def details(request, pk):
    pass


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def watchlists(request):
    pass


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def watchlist(request, pk):
    pass


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_mounted(request, pk):
    pass


