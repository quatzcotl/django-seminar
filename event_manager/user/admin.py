from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class MyUserAdmin(UserAdmin):
    # das eigene User-Model in user.models hat ein Feld address definiert (siehe models.py)
    # um es in der Administration freizuschalten, muss es hier angegeben werden.
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("address",)}),)
