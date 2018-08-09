from django.forms import ModelForm
from .models import Tweet, PrivateMessage, Comment


class TweetForm(ModelForm):
    class Meta:
        model = Tweet
        exclude = ['creation_date', 'user']


class PrivateMessageForm(ModelForm):
    class Meta:
        model = PrivateMessage
        exclude = ['sent_date', 'sender', 'is_read']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['creation_date', 'user', 'tweet']