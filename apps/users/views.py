from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from apps.users.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
import logging
from django.views.generic import UpdateView
from django.views import View
from .models import UserProfile
from django.utils.translation import gettext_lazy as _


logger = logging.getLogger(__name__)


# class UserUpdateView(View):
#     def patch(self, request):
#         obj = get_object_or_404(UserProfile, id=id)
#         form = UserForm(request.POST or None, instance=obj)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("profile_data")
#         context = {'form': form}
#         return render(request, 'update.html', context)


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = UserProfile
    success_message = _("Information successfully updated")
    template_name = 'user_profile.html'
    form_class = UserForm

    def get_success_url(self):
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


class UserProfileView(View):
    def get(self, request):
        form = UserForm()  # Create an empty form
        userprofile = UserProfile.objects.all()
        context = {'userprofile': userprofile, 'form': form}
        return render(request, 'users/profile_create.html', context)

    def post(self, request):
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('users:dashboard')
        else:
            userprofile = UserProfile.objects.all()
            context = {'userprofile': userprofile, 'form': form}
            return render(request, 'create.html', context)


def profile_view(request):
    return render(request, 'user_profile.html')


# def sign_up(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save()
#             return redirect('login')
#     else:
#         form = UserForm()
#     context = {'form': form}
#     return render(request, 'signup.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log the user in
            user = form.get_user()
            login(request, user)
            return redirect('users:dashboard')  # Redirect to the user's profile page
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def dashboard(request):
    user_entries = UserProfile.objects.all()
    context = {'user_entries': user_entries}
    return render(request, 'dashboard.html', context)
