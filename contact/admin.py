from django.contrib import admin
from contact.models import UserData


@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_on']