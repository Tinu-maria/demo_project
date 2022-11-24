from django.db import models

# Create your models here.

class Feedback(models.Model):
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.email