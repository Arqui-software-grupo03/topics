from rest_framework import viewsets
from .models import Topic, Post, Subscriber
from .serializers import TopicSerializer, PostSerializer, SubscriberSerializer
from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows post ids to be viewed.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(topic=self.kwargs['topic'])

class SubscriberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows post ids to be viewed.
    """
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    def get_queryset(self):
        return Subscriber.objects.filter(topic=self.kwargs['topic'])
