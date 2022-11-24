from django.test import TestCase
from feedback.models import Feedback

# Create your tests here.

class FeedbackTesting(TestCase):
    def setUp(self):
        Feedback.objects.create(email="test1@gmail.com", message="hello")
        Feedback.objects.create(email="test2@gmail.com", message="hai")
    
    def test_feedback(self):
        feedback1 = Feedback.objects.get(email="test1@gmail.com")
        feedback2 = Feedback.objects.get(email="test2@gmail.com")
        self.assertEqual(str(feedback1), "test1@gmail.com")
        self.assertEqual(str(feedback2), "test2@gmail.com")