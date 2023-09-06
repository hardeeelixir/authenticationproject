# from django.conf.urls import url
from django.urls import path

from apps.users import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup, name='signup'),
    # path('home', views.home, name='home'),
    # path('cards', views.cards, name='cards'),
    path('base', views.base, name='base'),
    path('support', views.support, name='support'),
    path('support_file', views.support_file, name='support_file'),
    # path('signin', views.signin,name='signin'),
    # path('login', views.login,name='login'),
]
