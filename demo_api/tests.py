from django.test import TestCase
from demo_api.models import Student
from unittest import mock
from demo_api.functions import mock_student
from django.urls import reverse
from demo_api.factories import UserFactory, ProfileFactory, StudentFactory

# Factories

class ProfilelistTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.profile = ProfileFactory(user = self.user)
        self.url = reverse('profile-get')
        
    def testbook(self):
        profile1 = ProfileFactory(user = self.user)
        profile2 = ProfileFactory(user = self.user)
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertContains(response, profile1.name)
        self.assertContains(response, profile2.name)

class StudentlistTest(TestCase):
    def setUp(self):
        self.student = StudentFactory()
        self.url = reverse('student-get')
        
    def testbook(self):
        student1 = StudentFactory()
        student2 = StudentFactory()
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertContains(response, student1.first_name)
        self.assertContains(response, student2.first_name)
        print('Name is', student2.first_name)

# Mock test

def mock_name():  
    return Student(first_name = 'tinu', last_name = 'maria')

class TestStudentModel(TestCase):
    @mock.patch('demo_api.functions.get_student', mock_name)
    def test_student_model(self):
        self.assertEqual(mock_student().full_name, 'tinu maria')
        print('Name is', mock_student().full_name)

