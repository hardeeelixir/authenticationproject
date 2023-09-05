from django.db import models
from django.contrib.auth.models import User, AbstractUser

# from django.contrib.auth import get_user_model


# Create your models here.

class UseProfile(AbstractUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    phone_number = models.IntegerField(max_length=20,  blank=True, null=True, default='1234567890')


    def __str__(self):
        return self.user

    class Meta:
        app_label = 'User profil'
