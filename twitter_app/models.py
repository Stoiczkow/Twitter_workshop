from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tweet(models.Model):
    text = models.TextField(max_length=140)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=True)


class Comment(models.Model):
    text = models.TextField(max_length=140)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=True)
    tweet = models.ForeignKey(Tweet, on_delete=True)
