# from django.conf.urls import url
from django.urls import path

from apps.users import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('login', views.login_view, name='login'),
]
