from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('cards', views.cards, name='cards'),
    path('base', views.base, name='base'),
    path('support', views.support, name='support'),
    path('support_file', views.support_file, name='support_file'),
    path('signin', views.signin,name='signin'),
    path('login', views.login,name='login'),
]
