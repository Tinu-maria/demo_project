from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.

class UserTesting(TestCase):
    def setUp(self):
        User.objects.create(username="test1", password="test")
        User.objects.create(username="test2", password="test")
    
    def test_user(self):
        user1 = User.objects.get(username="test1")
        user2 = User.objects.get(username="test2")
        self.assertEqual(str(user1), "test1")
        self.assertEqual(str(user2), "test2")