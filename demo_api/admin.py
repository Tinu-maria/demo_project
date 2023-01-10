from django.contrib import admin
from demo_api.models import UserProfile, Student

# Register your models here.

admin.site.register(Student)
admin.site.register(UserProfile)
