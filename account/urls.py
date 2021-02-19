from django.conf.urls import url
from django.urls import path
from account import views
from account.views import index

app_name = "account"

urlpatterns = [
    path('', views.index, name='index'),
    path('show/<int:form_id>/', views.show, name='show'),
    # url('', views.index, name='index')
]