from rest_framework import serializers
from .models import Topic, PostId, Subscriber

class PostIdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostId
        fields = ['post_id', 'topic']

    def create(self, validated_data):
        post_id = PostId.objects.create(post_id=validated_data['post_id'],
                                        topic=validated_data['topic'])
        return post_id

class SubscriberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['user_id', 'topic']

    def create(self, validated_data):
        subscriber = Subscriber.objects.create(user_id=validated_data['user_id'],
                                        topic=validated_data['topic'])
        return subscriber

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    post_ids = PostIdSerializer(required=False, many = True)
    subscribers = SubscriberSerializer(required=False, many=True)

    class Meta:
        model = Topic
        fields = ['id', 'title', 'description', 'post_ids', 'subscribers']
