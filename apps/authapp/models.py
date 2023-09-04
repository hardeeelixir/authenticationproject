from django.db import models
from django.db.models import Model
#from django.contrib.auth.models import User

# Create your models here.
class User(Model):
    name = models.CharField(max_length=255, default="your name")
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name
