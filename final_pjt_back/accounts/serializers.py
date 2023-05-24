from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    # article_set = 아티클 셋, 코멘트셋, watchlist 불러서 알고리즘 작성할 것
    # 알고리즘 작성은 backend에서 진행 예정
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'profile_img', 'profile_message', 'followers', 'preferences')

class FollowingSerializer(serializers.ModelSerializer):
    followings = UserSerializer(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'profile_img')
    