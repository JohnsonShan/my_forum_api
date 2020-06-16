from rest_framework import serializers
from posts.models import Post, Comment
from django.contrib.auth.models import User


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        fields = ['url', 'id', 'content', 'owner', 'post']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.StringRelatedField(many=True)
    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'content', 'owner', 'comments']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='post-detail')

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'posts']