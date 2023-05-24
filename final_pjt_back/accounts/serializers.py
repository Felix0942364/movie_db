from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'profile_img', 'profile_message', 'followers', 'preferences')

class FollowingSerializer(serializers.ModelSerializer):
    followings = UserSerializer(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'profile_img')
    