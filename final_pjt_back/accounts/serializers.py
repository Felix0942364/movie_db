from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.models import Article, Comment
from movies.serializers import WatchListSerializer

class UserSimplifiedSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'profile_img')

class ArticleSimplifiedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('author', 'id', 'title')

class CommentSimplifiedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'article', 'content')

class ProfileSerializer(serializers.ModelSerializer):
    followers = UserSimplifiedSerializer(many=True, read_only=True)
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)
    following = UserSimplifiedSerializer(many=True, read_only=True)
    following_count = serializers.IntegerField(source='following.count', read_only=True)
    articles = ArticleSimplifiedSerializer(many=True, read_only=True)
    comments = CommentSimplifiedSerializer(many=True, read_only=True)
    liked_articles = ArticleSimplifiedSerializer(many=True, read_only=True)
    liked_comments = CommentSimplifiedSerializer(many=True, read_only=True)
    
    watchlists = WatchListSerializer(many = True, read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'profile_img',
            'profile_message',
            'preferences',
            'followers_count',
            'followers',
            'following_count',
            'following',
            'articles',
            'comments',
            'liked_articles',
            'liked_comments',
            'watchlists',
        )

class FollowingSerializer(serializers.ModelSerializer):
    followings = UserSimplifiedSerializer(read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'profile_img')
    