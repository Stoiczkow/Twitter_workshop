from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect


class MainPageView(View):
    def get(self, request):
        ctx = {}
        return render(request, 'twitter_app/index.html', ctx)


class RegisterView(CreateView):
    model = User
    fields = ('email', 'username', 'password')
    template_name = 'registration/user_form.html'

    def post(self, request):
        user, created = User.objects.get_or_create(username=request.POST['username'])
        if created:
            # user was created
            # set the password here
            user.set_password(request.POST['password'])
            user.email = request.POST['email']
            user.save()
            return HttpResponseRedirect(reverse('login'))