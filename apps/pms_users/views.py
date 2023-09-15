from django.shortcuts import render
from apps.pms_users.models import *


# Create your views here.
def home_view(request):
    datas = PmsData.objects.all()
    context = {'task': 0,
               'events': 0,
               'posts': 0,
               'datas': datas}
    return render(request, 'pms/home.html', context)
