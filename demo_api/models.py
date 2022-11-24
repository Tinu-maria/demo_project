from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50, null=True)
    dob = models.DateField(null=True)
    bio = models.CharField(max_length=100, null=True)


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.first_name