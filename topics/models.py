from django.db import models

class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)

    def __str__(self):
        return self.title

    def add_post(self, post_id):
        self.post_id_set.create(post_id = post_id)

class PostId(models.Model):
    post_id = models.IntegerField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.post_id
