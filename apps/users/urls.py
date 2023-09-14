from django.urls import path

from apps.users import views

app_name = 'users'
urlpatterns = [
    # path('signup', views.sign_up, name='signup'),
    path('login', views.login_view, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile_data', views.profile_view, name='profile_data'),
    path('', views.UserSignUpView.as_view(), name="user_signup"),
    # path('/ (?P<id>\w+)/$', views.UserProfileView.as_view(), name="user_profile"),
    path('userprofile/<int:id>/', views.UserProfileView.as_view(), name="user_profile"),
    # path('update', UserUpdateView.as_view()),
    path('logout', views.logout_view, name='logout'),
    path('test', views.test, name='test'),
    path('newlogin', views.newlogin, name='newlogin')
]
