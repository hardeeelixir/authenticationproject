# from django.conf.urls import url
from django.urls import path

from apps.users import views
from apps.users.views import UserProfileView, UserUpdateView

app_name = 'users'
urlpatterns = [
    # path('signup', views.sign_up, name='signup'),
    path('login', views.login_view, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile_data', views.profile_view, name='profile_data'),

    path('update', UserUpdateView.as_view()),
    path('', views.UserProfileView.as_view()),
]
