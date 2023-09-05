from django import forms
from .models import UseProfile
from django.contrib.auth.forms import UserCreationForm



class CustomUserCreation(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    bio = forms.CharField(max_length=100, required=False)
    profile_picture = forms.ImageField(required=False)

    phone_number = forms.CharField(required=False)
    # phone = PhoneNumberField()
    class Meta:
        model = UseProfile
        fields = ('first_name', 'username', 'email', 'password1', 'password2', 'phone_number')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']

        if self.cleaned_data['bio']:
            user.profile.bio = self.cleaned_data['bio']
        if self.cleaned_data['profile_picture']:
            user.profile.profile_picture = self.cleaned_data['profile_picture']
        # if self.cleaned_data['mobile_number']:
        #     user.profile.mobile_number = self.cleaned_data['mobile_number']

        if commit:
            user.save()

        return user
