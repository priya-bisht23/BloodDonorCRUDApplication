# blooddonor/models.py

from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=5)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name
