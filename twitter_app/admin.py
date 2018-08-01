from django.contrib import admin
from .models import Tweet
# Register your models here.


@admin.register(Tweet)
class AuthorAdmin(admin.ModelAdmin):
    pass