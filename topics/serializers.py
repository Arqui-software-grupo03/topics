from rest_framework import serializers
from .models import Topic, PostId

class PostIdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostId
        fields = ['post_id', 'topic_identifier', 'topic']

    def create(self, validated_data):
        post_id = PostId.objects.create(post_id=validated_data['post_id'],
                                        topic_identifier=validated_data['topic_identifier'],
                                        topic = Topic.objects.get(id = validated_data['topic_identifier']))
        return post_id

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    post_ids = PostIdSerializer(required=False, many = True)

    class Meta:
        model = Topic
        fields = ['id', 'title', 'description', 'post_ids']
