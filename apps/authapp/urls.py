# from django.conf.urls import url
from django.urls import path

from apps.authapp import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('login', views.login, name='login'),
]
