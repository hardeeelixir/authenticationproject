from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.

def home(request):

    initial_data = {'name':'Hardee',
                    'email':'hardee@gmail.com',
                    'password':123}
    form = UserForm(initial=initial_data)
    context = {'form':form}
    return render(request, 'home.html', context)

def signup(request):
    return render(request, 'signup.html')

def cards(request):
    return render(request, 'cards.html')

def base(request):
    return render(request, 'base.html')

def support(request):
    return render(request, 'support.html')

def support_file(request):
    return render(request, 'support_file.html')

def signin(request):
    return render(request, 'signin.html')

def login(request):
    return render(request,'login.html')