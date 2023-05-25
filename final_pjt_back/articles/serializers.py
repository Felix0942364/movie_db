from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    like_count = serializers.IntegerField(source='liking_users.count', read_only=True)
    author_name = serializers.CharField(source='author.username', read_only=True)
    class Meta:
        model = Article
        # fields = ('id', 'title', 'content')
        fields = ('id', 'author', 'title', 'content', 'username', 'like_count', 'created_at', 'author_name')


class CommentSerializer(serializers.ModelSerializer):
    comment_likes_count = serializers.IntegerField(source = 'liking_users.count', read_only=True)
    author_name = serializers.CharField(source='author.username', read_only=True)
    # user_likes = serializers.BooleanField()

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article', 'author')


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    # username = serializers.CharField(source='user.username', read_only=True)
    article_likes_count = serializers.IntegerField(source = 'liking_users.count', read_only=True)
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('author',)

