from django.conf.urls import url
from django.urls import path
from account import views
from account.views import index

urlpatterns = [
    path('', views.index, name='index'),
    url('', views.show, name='show'),
    # url('', views.index, name='index')
]