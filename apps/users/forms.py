from crispy_forms.bootstrap import StrictButton
from django import forms
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import BigIntegerField

from apps.users.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Column, Row, Div


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


class UserUpdateForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
            # exclude = ['password1']


class UserUpdateChild(ModelForm):
    user = UserUpdateForm()

    class Meta:
        model = User
        fields = '__all__'


# class CrispyLoginForm(forms.Form):
#     fistname = forms.CharField()
#     lastname = forms.CharField()
#     username = forms.CharField()
#     email = forms.EmailField()
#     password = forms.PasswordInput()
#     address1 = forms.CharField()
#     address2 = forms.CharField()
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#   Row(
#          Column('fistname', css_class='form-group col-md-12 mb-0'),
#                 Column('lastname', css_class='form-group col-md-6 mb-0'),
#                 css_class='form-row'
#                 ),
#                 'username'
#                 'email',
#
#          Row(
#            Column('address1', css_class='form-group col-md-6 mb-0'),
#                   Column('address2', css_class='form-group col-md-6 mb-0')
#               ),
#
#             Submit('submit', 'Submit')
#         )




class CrispyLoginForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    address1 = forms.CharField(label='Address 1')
    address2 = forms.CharField(label='Address 2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        # self.helper.layout = Layout(
        #     'email',
        #     'password',
        #     'remember_me',
        #     StrictButton('Sign in', css_class='btn-default'),
        # )

        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'username',
            'email',
            Row(
                Column('password', css_class='col-md-6'),
                Column('address1', css_class='col-md-6'),
                css_class='form-row'
            ),
            'address2'
            # Submit('submit', 'Submit')
        )


class BasicForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    address1 = forms.CharField(label='Address 1')
    address2 = forms.CharField(label='Address 2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('first_name', css_class='form-group col-4'),
                Div('last_name', css_class='form-group col-4'),
                Div('email', css_class='form-group col-4'),
                css_class='form-row'
            ),
            Div(
                Div('password', css_class='form-group col-4'),
                Div('confirm_password', css_class='form-group col-4'),
                css_class='form-row'
            ),
            # Div(
            #     Div('gender', css_class='form-group col-4'),
            #     Div('phone_number', css_class='form-group col-8'),
            #     css_class='form-row'
            # ),
            # 'about_you',
            Submit('submit', 'Sign up', css_class='mt-4')
        )
