from django.db import models

# Create your models here.
class register(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField()
    role = models.CharField(max_length=100)
    Password = models.CharField(max_length=10)
    C_Password = models.CharField(max_length=10)