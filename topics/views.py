from rest_framework import viewsets
from .models import Topic, PostId, Subscriber
from .serializers import TopicSerializer, PostIdSerializer, SubscriberSerializer
from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class PostIdViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows post ids to be viewed.
    """
    queryset = PostId.objects.all()
    serializer_class = PostIdSerializer

    # def get_queryset(self):
    #     return PostId.objects.filter(topic=self.kwargs['topic'])

class SubscriberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows post ids to be viewed.
    """
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    # def get_queryset(self):
    #     return Subscriber.objects.filter(topic=self.kwargs['topic'])
