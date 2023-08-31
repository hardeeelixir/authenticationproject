from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('', views.sign, name='sign'),
    path('cards', views.cards, name='cards'),
    path('base', views.base, name='base'),
    path('support', views.support, name='support'),
    path('support_file', views.support_file, name='support_file')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
