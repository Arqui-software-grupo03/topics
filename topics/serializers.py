from rest_framework import serializers
from .models import Topic, PostId

class PostIdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostId
        # fields = '__all__'
        fields = ['post_id', 'topic']

    def create(self, validated_data):
        #post_id = validated_data['topic'].postId_set.create(post_id=validated_data['post_id'])
        post_id = PostId.objects.create(post_id=validated_data['post_id'],
                                        topic=validated_data['topic'])
        return post_id

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    post_ids = PostIdSerializer(required=False, many = True)

    class Meta:
        model = Topic
        fields = ['id', 'title', 'description', 'post_ids']

    # def add_post(self, instance, validated_data):
    #     instance.postid_set.create(**validated_data)
    #     return instance.post_id_set
