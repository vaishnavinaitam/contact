from django.db import models

# Create your models here.
class Contact(models.Model):
    stname = models.CharField(max_length=50)
    phno = models.IntegerField()
    email = models.EmailField()
    add = models.CharField(max_length=50)