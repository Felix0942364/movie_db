from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import UserSerializer, FollowingSerializer


@api_view(['GET', 'POST'])
def profile(request, user_pk):
    if request.method == 'GET':
        user = get_object_or_404(get_user_model(), pk = user_pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'POST':
        if (request.user.pk != user_pk):
            return Response({"you couldn't edit none but your profile"})
        user = get_object_or_404(get_user_model(), pk = request.user)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def follower(request, user_pk):
    user = get_object_or_404(get_user_model(), pk = user_pk)
    serializer = FollowingSerializer(user)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def following(request, user_pk):
    if request.method == 'GET':
        user = get_object_or_404(get_user_model(), pk=user_pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'POST':
        if (request.user.pk == user_pk):
            return Response()
        user = get_object_or_404(get_user_model(), pk=user_pk)
        if user.followers.filter(pk=request.user.pk).exists():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)
        serializer = UserSerializer(user)
        return Response(serializer.data)
