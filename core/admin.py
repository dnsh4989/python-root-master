from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Article


class SuperUser(UserAdmin):
    ordering = ['id']


admin.site.register(User, SuperUser)
admin.site.register(Article)