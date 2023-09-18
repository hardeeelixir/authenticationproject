from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


# def validate_phone_number(value):
#     if not value.isdigit():
#         raise ValidationError("Please enter phone number in digits")
#     if len(value) != 10:
#         raise ValidationError("Your number should be of ten digits")
#

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    bio = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    phone_number = models.CharField(max_length=10)

    # REQUIRED_FIELDS = ['username']
    # USERNAME_FIELD = 'user.username'

    def __str__(self):
        return self.user.username

    @property
    def email(self):
        return "%s"%(self.user.email)
    def clean(self):
        if self.phone_number:
            try:
                mobile = int(self.phone_number)
            except:
                raise ValidationError(
                    {"phone_number": "phone number should be int."}
                )
        if not self.phone_number.isdigit():
            raise ValidationError("Please enter phone number in digits")
        if len(self.phone_number) != 10:
            raise ValidationError("Your number should be of ten digits")


    # @staticmethod
    # def validate_phone_number(self, value):
    #     if not value.isdigit():
    #         raise ValidationError("Please enter phone number in digits")
    #     if len(value) != 10:
    #         raise ValidationError("Your number should be of ten digits")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        db_table = 'userprofile'



