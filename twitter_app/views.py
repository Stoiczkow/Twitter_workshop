from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from .models import Tweet, Comment, Profile, PrivateMessage
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import TweetForm, PrivateMessageForm


class MainPageView(View):
    def get(self, request):
        tweets = Tweet.objects.all().order_by('-creation_date')
        comments = Comment.objects.all().order_by('-creation_date')

        form = TweetForm()
        ctx = {'tweets': tweets,
               'form': form,
               'comments': {},
               'comments_text': comments}

        for tweet in tweets:
            for comment in comments:
                if comment.tweet == tweet:
                    try:
                        ctx['comments'][tweet.pk] += 1
                    except:
                        ctx['comments'][tweet.pk] = 1

        return render(request, 'twitter_app/index.html', ctx)

    def post(self, request):
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = Tweet.objects.create(text=request.POST['text'],
                                         user=request.user)
            return HttpResponseRedirect(reverse('index'))


class RegisterView(CreateView):
    model = User
    fields = ('email', 'username', 'password')
    template_name = 'registration/user_form.html'

    def post(self, request):
        user, created = User.objects.get_or_create(username=request.POST['username'])
        if created:
            user.set_password(request.POST['password'])
            user.email = request.POST['email']
            user.save()
            return HttpResponseRedirect(reverse('login'))


class EditProfile(UpdateView):
    model = Profile
    fields = ['bio', 'location', 'birth_date']
    template_name = 'registration/user_update.html'
    success_url = '/'


class PrivateMessageView(View):
    def get(self, request):
        form = PrivateMessageForm()
        ctx = {'form': form}
        return render(request, 'twitter_app/pm_form.html', ctx)

    def post(self, request):
        form = PrivateMessageForm(request.POST)
        if form.is_valid():
            pm = PrivateMessage.objects.create(text=request.POST['text'],
                                               recipient=User.objects.get(pk=request.POST['recipient']),
                                               sender=request.user)
            return HttpResponseRedirect(reverse('index'))


class Inbox(View):
    def get(self, request):
        recieved = PrivateMessage.objects.filter(recipient=request.user)
        sent = PrivateMessage.objects.filter(sender=request.user)
        ctx = {}
        return render(request, 'twitter_app/inbox.html', ctx)