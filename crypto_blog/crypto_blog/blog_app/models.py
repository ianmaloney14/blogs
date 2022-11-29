from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="title")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=255, default="In this article...")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # thumbnail = models.ImageField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
