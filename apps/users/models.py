from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    bio = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    # phone_number = models.CharField(validators=[RegexValidator('[789][0-9]{9}',
    #                             message="Enter a valid 10 digit contact number")])

    phone_number = models.CharField(max_length=10, blank=True, null=True)

    # REQUIRED_FIELDS = ['username']
    # USERNAME_FIELD = 'user.username'

    def __str__(self):
        return self.user.username

    def clean(self):
        if self.phone_number:
            try:
                mobile = int(self.phone_number)
            except:
                raise ValidationError
        return

    # def validation(phone_number):
    #     if phone_number.length == 10 && :
    #         return phone_number
    #     else:
    #         raise ValidationError("This field accepts 10 digit number")

    class Meta:
        db_table = 'userprofile'