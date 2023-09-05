from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CustomUserCreation  # Updated import

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreation(request.POST)
        try:
            if form.is_valid():
                user = form.save()
                return redirect('profile')  # Use the correct URL name here
        except Exception as e:
            print(e)
    else:
        form = CustomUserCreation()  # Instantiate the form without arguments
    context = {'form': form}  # Change 'user' to 'form' in the context dictionary
    # context = {}  # Change 'user' to 'form' in the context dictionary
    return render(request, 'signup.html', context)

def profile(request):
    return redirect('profile')
