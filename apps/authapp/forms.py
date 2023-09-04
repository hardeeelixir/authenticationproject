from django.forms import ModelForm

# from django.forms import forms
from .models import *

class UserForm(ModelForm):
        class Meta:
            model = User
            fields = '__all__'