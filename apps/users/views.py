from django.shortcuts import render, redirect
from apps.users.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'signup.html', context)


def profile(request):
    return render(request, 'profile.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log the user in
            user = form.get_user()
            login(request, user)
            return redirect('support_file')  # Redirect to the user's profile page
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def base(request):
    return render(request, 'base.html')


def home(request):
    initial_data = {'name': 'Hardee',
                    'email': 'hardee@gmail.com',
                    'password': 123}
    form = UserForm(initial=initial_data)
    context = {'form': form}
    return render(request, 'home.html', context)


def support(request):
    user_entries = UserProfile.objects.all()
    context = {'user_entries': user_entries}
    return render(request, 'support.html', context)


def support_file(request):
    user_entries = UserProfile.objects.all()
    context = {'user_entries': user_entries}
    return render(request, 'support_file.html', context)


def cards(request):
    return render(request, 'cards.html')
