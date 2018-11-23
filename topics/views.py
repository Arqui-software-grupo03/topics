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

        # Get URL parameter as a string, if exists
        user_id = self.request.query_params.get('user_id', None)

        # Get snippets for ids if they exist
        if user_id is not None:
            # Convert parameter string to list of integers
            # user_id = [ int(x) for x in user_id.split(',') ]
            # Get objects for all parameter ids
            queryset = Subscriber.objects.filter(topic=self.kwargs['topic'], user_id=user_id)

        else:
            # Else no parameters, return all objects
            queryset = Subscriber.objects.filter(topic=self.kwargs['topic'])

        return queryset


    # def get_queryset(self):
    #     return Subscriber.objects.filter(topic=self.kwargs['topic'])
