from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import *


class UserInline(admin.StackedInline):
    model = User


class UserAdmin(admin.ModelAdmin):
    inlines = [
        UserInline,
    ]
    list_display = ["username", "account_approved","parent","is_teamleader"]


admin.site.register(User, UserAdmin)
