from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Feedback(models.Model):
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.email

class Profile(models.Model):
    # name = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(upload_to='images', null=True, blank=True)

