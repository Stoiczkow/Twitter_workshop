from django.forms import ModelForm
from .models import Tweet, PrivateMessage


class TweetForm(ModelForm):
    class Meta:
        model = Tweet
        exclude = ['creation_date', 'user']


class PrivateMessageForm(ModelForm):
    class Meta:
        model = PrivateMessage
        exclude = ['sent_date', 'sender', 'is_read']