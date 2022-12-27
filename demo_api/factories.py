import factory
from django.contrib.auth.models import User
from faker import Factory
from demo_api.models import UserProfile, Student

faker = Factory.create()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = faker.name()
    email = faker.email()

class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserProfile
    name = faker.word()
    gender = faker.word()
    bio = faker.word()
    user = factory.SubFactory(UserFactory)

class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student
    first_name = faker.name()
    last_name = faker.name()
    email = faker.email()
    course = faker.word()