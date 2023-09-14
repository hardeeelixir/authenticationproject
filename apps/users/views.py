from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from apps.users.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
import logging
from django.views.generic import UpdateView
from django.views import View
from .models import UserProfile
from django.urls import reverse_lazy
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


# class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     model = UserProfile
#     success_message = _("Information successfully updated")
#     template_name = 'user_profile.html'
#     form_class = UserForm
#
#     def get_success_url(self):
#         return self.request.user.get_absolute_url()
#
#     def get_object(self):
#         return self.request.user


class UserSignUpView(View):
    template_name = 'users/profile_create.html'

    def get(self, request):
        form = UserForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('/login')
        else:
            context = {'form': form}
            return render(request, self.template_name, context)


# @login_required(redirect_field_name='login')
class UserProfileView(View):
    template_name_patch = 'user_profile.html'

    def get(self, request, id):
        form = UserUpdateChild(instance=request.user)
        context = {'form': form}
        return render(request, self.template_name_patch, context)

    def patch(self, request, id):
        user_instance = get_object_or_404(User, id=id)
        form = UserUpdateChild(request.PATCH, request.FILES, instance=user_instance)
        if form.is_valid():
            user = form.save()
            return redirect('users:dashboard')
        context = {'form': form}
        return render(request, self.template_name_patch, context)


@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return redirect('users:login')


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
            user = form.get_user()
            login(request, user)
            return redirect('users:dashboard')  # Redirect to the user's profile page
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)


@login_required(login_url='/login')
def dashboard(request):
    user_entries = UserProfile.objects.all()
    context = {'user_entries': user_entries}
    return render(request, 'dashboard.html', context)


@login_required(login_url='/login')
def test(request):
    return render(request, 'test.html')


def newlogin(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users:dashboard')  # Redirect to the user's profile page
    else:
        form = BasicForm()
    context = {'form': form}
    return render(request, 'newlogin.html', context)

