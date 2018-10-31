from django.db import models

class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)

    def __str__(self):
        return self.title

class PostId(models.Model):
    post_id = models.IntegerField(unique=True, primary_key=True)
    topic = models.ForeignKey(Topic,
                              on_delete=models.CASCADE,
                              related_name='post_ids'
                              )

    def __str__(self):
        return self.post_id
