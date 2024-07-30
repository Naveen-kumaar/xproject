from django.db import models

# Create your models here.
class register(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField()
    role = models.CharField(max_length=100)
    Password = models.CharField(max_length=10)
    C_Password = models.CharField(max_length=10)


class patientdetails(models.Model):
    Date = models.DateField()
    Name = models.CharField(max_length=50)
    Age  = models.IntegerField()
    CHOICES =[
        ('male','male'),
        ('female','female')
    ]
    Gender = models.CharField(max_length=10,choices=CHOICES,null= False,blank=False)
    Address =models.TextField()
    Contactno = models.IntegerField()
    History = models.CharField(max_length=100)
    Pain = models.CharField(max_length=100)
    Duration =models.TimeField()

