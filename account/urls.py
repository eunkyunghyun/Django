from django.urls import path
from account.views import index

urlpatterns = [
    path('main/', index, name='index'),
]