from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from posts.permissions import IsOwnerOrReadOnly
from posts.models import Post, Comment
from posts.serializers import PostSerializer, UserSerializer, CommentSerializer

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework import generics
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format)
    })

