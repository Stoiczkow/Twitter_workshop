from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from .models import Tweet, Comment
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from .forms import TweetForm


class MainPageView(View):
    def get(self, request):
        tweets = Tweet.objects.all().order_by('-creation_date')
        comments = Comment.objects.all().order_by('-creation_date')
        form = TweetForm()
        ctx = {'tweets': tweets,
               'form': form,
               'comments': {}}

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
    model = User
    fields = ['first_name', 'last_name']
    template_name = 'registration/user_update.html'
    success_url = '/'