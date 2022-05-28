from django.contrib import admin

# Register your models here.
from Accounts.models import Accounts

@admin.register(Accounts)
class AndroidAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'identify',
        'password'
    )