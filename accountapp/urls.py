from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp import views
from account.views import index
from accountapp.views import AccountCreateView

app_name = "accountapp"

urlpatterns = [
    path('create/', AccountCreateView.as_view(), name='create'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('success/', views.success, name='success'),
    path('main/', views.main, name='main'),
]