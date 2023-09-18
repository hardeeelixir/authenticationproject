from django.urls import path
from apps.pms_users import views

app_name = ''
urlpatterns = [
    path('home', views.home_view, name='home'),

]
