from django.db import models
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    