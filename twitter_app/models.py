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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class PrivateMessage(models.Model):
    text = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    received_date = models.DateTimeField(null=True)
    sender = models.ForeignKey(User, on_delete=True, related_name='sender')
    recipient = models.ForeignKey(User, on_delete=True, related_name='recipient')