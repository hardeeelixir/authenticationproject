from django.db import models

# Create your models here.
class PmsData(models.Model):

    # status = models.CharField(max_length=1, default='P', choices=STATUS_CHOICES)
    username = models.CharField(max_length=100, blank=True, null=True)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    # birthday = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.username


