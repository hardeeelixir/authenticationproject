# from django.conf.urls import url
from django.urls import path

from . import views
urlpatterns = [
    path('', views.signup, name='signup'),
    path('profile',views.profile,name='profile'),
]