from django.contrib.auth.models import User
from demo_api.models import Student, UserProfile
from django.db.models import F, Q, Value, CharField, Sum, Avg
from django.db.models.functions import Concat
from django.shortcuts import get_object_or_404

qs = Student.objects.get(id=27)
qs = Student.objects.all()

qs = Student.objects.filter(id__gte=27)
qs = Student.objects.filter(id__gte=27).values()
qs = Student.objects.filter(first_name__startswith='S').values()
qs = Student.objects.filter(course__contains='python').count()

qs = get_object_or_404(Student, id=27)
qs = Student.objects.get(id__exact=27)
qs = Student.objects.get(id__iexact=27)
qs = Student.objects.filter(course__isnull=True)

name = Student.objects.annotate(full_name=Concat(F('first_name'), Value(' '), F('last_name'), output_field=CharField()))
age = Student.objects.aggregate(new_age=Sum(F('age') + 1))
age = Student.objects.aggregate(new_age=Avg(F('age')))
data = Student.objects.filter(Q(id=27))

obj, created = Student.objects.get_or_create(
    first_name='tinu',
    last_name='maria',
    defaults={'email': 'name@gmail.com'},
)

qs = UserProfile.objects.select_related('user')
qs = UserProfile.objects.prefetch_related('user')

Student.objects.defer("age", "email")
Student.objects.only("course")

name = User.objects.annotate(age=User(F('age')))
name = User.objects.annotate(full_name=Concat(F('first_name'), Value(' '), F('last_name'), output_field=CharField()))
name = User.objects.aggregate(full_name=Sum(F('first_name') + F('last_name'), output_field=CharField()))

data1 = Student.objects.filter(Q(id=27))

mydata = User.objects.filter(username__startswith='S').values()
mydata = User.objects.filter(id__gte=3).values()

obj, created = User.objects.get_or_create(
    first_name='tinu',
    last_name='maria',
    defaults={'email': 'name@gmail.com'},
)

User.objects.values('id', 'headline')  # return as dictionary
User.objects.values_list('id', 'headline')  # return as tuple

User.objects.filter(
    username__isnull=True)  # Takes either True or False, which correspond to SQL queries of IS NULL and IS NOT NULL

user = get_object_or_404(User, id=3)

User.objects.get(id__exact=14)  # Exact match
User.objects.get(id__iexact=14)  # Case-insensitive exact match

User.objects.defer("age", "email")
User.objects.only("name")

e = User.objects.select_related('user').get(id=5)
e = User.objects.prefetch_related('user')
# for foreign key relationship, use select_related; and 
# for M2M relationship, use prefetch_related

User.objects.get('email').contains()  # Returns True if the QuerySet contains obj, and False if not
User.objects.get('email').contains()  # Returns True if the QuerySet contains any results, and False if not
