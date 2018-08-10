"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitter_app.views import MainPageView, RegisterView, EditProfile, PrivateMessageView, Inbox, ChangeMsgStatus
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/login/'}, name='logout'),
    path('edit_profile/<pk>', EditProfile.as_view(), name='edit_profile'),
    path('prv_msg/', PrivateMessageView.as_view(), name='prv_msg'),
    path('inbox/', Inbox.as_view(), name='inbox'),
    path('change_msg/', ChangeMsgStatus.as_view()),
]
