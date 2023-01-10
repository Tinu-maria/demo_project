from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50, null=True)
    dob = models.DateField(null=True)
    bio = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField(null=True)
    course = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.first_name

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    # @property
    # def email(self):  
    #     return '{}.{}@gmail.com'.format(self.first_name,self.last_name)

    @full_name.setter
    def full_name(self, name):
        newfirst_name, newlast_name = name.split(' ')
        self.first_name = newfirst_name
        self.last_name = newlast_name

    @full_name.deleter
    def full_name(self):
        # print('deleted name')
        self.first_name = None
        self.last_name = None


obj = Student('', 'tinu', 'maria')
obj.full_name = 'maria tinu'

# print("First Name is:", obj.first_name)  
# print("Last Name is:", obj.last_name)
# print("Full Name is:", obj.full_name) 
# print("Full Name is:", obj.full_name())  

del obj.full_name
