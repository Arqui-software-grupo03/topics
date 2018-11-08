from django.db import models

class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)

    def __str__(self):
        return self.title

class Post(models.Model):
    post_id = models.IntegerField(unique=True, primary_key=True)
    topic_identifier = models.IntegerField(null=False)
    topic = models.ForeignKey(Topic,
                              null=True,
                              on_delete=models.CASCADE,
                              related_name='posts'
                              )

    def __str__(self):
        return self.post_id

class Subscriber(models.Model):
    user_id = models.IntegerField(unique=True, primary_key=True)
    topic_identifier = models.IntegerField(null=False)
    topic = models.ForeignKey(Topic,
                              null=True,
                              on_delete=models.CASCADE,
                              related_name='subscribers'
                              )

    def __str__(self):
        return self.user_id
