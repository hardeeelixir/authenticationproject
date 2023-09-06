from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    bio = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    # REQUIRED_FIELDS = ['username']
    # USERNAME_FIELD = 'user.username'

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'userprofile'