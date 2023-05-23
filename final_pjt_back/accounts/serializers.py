from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

class FollowingSerializer(serializers.ModelSerializer):
    followings = UserSerializer(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'profile_img')
    