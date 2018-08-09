from django.contrib import admin
from .models import Tweet, Comment, Profile, PrivateMessage
# Register your models here.


@admin.register(Tweet)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(PrivateMessage)
class AuthorAdmin(admin.ModelAdmin):
    pass