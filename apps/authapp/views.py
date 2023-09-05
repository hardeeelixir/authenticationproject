from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *  # Updated import
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreation(request.POST)
        try:
            if form.is_valid():
                user = form.save()
                return redirect('login')  # Use the correct URL name here
        except Exception as e:
            print(e)
    else:
        form = CustomUserCreation()  # Instantiate the form without arguments
    context = {'form': form}  # Change 'user' to 'form' in the context dictionary
    # context = {}  # Change 'user' to 'form' in the context dictionary
    return render(request, 'signup.html', context)

def profile(request):
    return render(request, 'profile.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log the user in
            user = form.get_user()
            login(request, user)
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)
