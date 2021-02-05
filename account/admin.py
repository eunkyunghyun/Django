from django.contrib import admin
from account.models import Data


class Auth(admin.ModelAdmin):
    list_display = ['id', 'name', 'text']
admin.site.register(Data, Auth)