from django import forms
from django.contrib.auth.models import User
from django.db import transaction

from apps.users.models import UserProfile
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    bio = forms.CharField(max_length=100, required=False)
    profile_picture = forms.ImageField(required=False)
    phone_number = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password1', 'password2', 'bio', 'profile_picture', 'phone_number')

    def save(self, commit=True):
        with transaction.atomic():
            user = super().save()
            user_profile = UserProfile.objects.create(
                user=user,
                bio=self.cleaned_data.get('bio'),
                profile_picture=self.cleaned_data.get('profile_picture'),
                phone_number=self.cleaned_data.get('phone_number', None)
            )
            return user
