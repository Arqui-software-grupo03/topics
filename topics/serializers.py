from rest_framework import serializers
from .models import Topic, Post, Subscriber

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['post_id', 'topic_identifier']

    def create(self, validated_data):
        post = Post.objects.create(post_id=validated_data['post_id'],
                                        topic_identifier=validated_data['topic_identifier'],
                                        topic = Topic.objects.get(topic_id = validated_data['topic_identifier']))
        return post

class SubscriberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['user_id', 'topic_identifier']

    def create(self, validated_data):
        subscriber = Subscriber.objects.create(user_id=validated_data['user_id'],
                                               topic_identifier=validated_data['topic_identifier'],
                                               topic = Topic.objects.get(topic_id = validated_data['topic_identifier']))
        return subscriber

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    posts = PostSerializer(required=False, many = True)
    subscribers = SubscriberSerializer(required=False, many=True, partial=True)

    class Meta:
        model = Topic
        fields = ['topic_id', 'title', 'description', 'posts', 'subscribers']
