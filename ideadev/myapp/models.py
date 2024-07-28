# models.py
from django.db import models

class Contact(models.Model):
    PURPOSE_CHOICES = [
        ('startup', 'Start-up'),
        ('personal', 'Personal'),
    ]

    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    purpose = models.CharField(max_length=10, choices=PURPOSE_CHOICES)
    message = models.TextField()

    def __str__(self):
        return self.name
