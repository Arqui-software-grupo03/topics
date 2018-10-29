from rest_framework import serializers
from .models import Topic

class TopicSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Topic
        fields = ['id', 'title', 'description']
