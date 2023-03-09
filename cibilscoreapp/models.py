from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=10)
    mobilenum = models.BigIntegerField()
    address=models.CharField(max_length=12)
    salary=models.IntegerField()
    dob=models.DateTimeField(auto_now=True)
    email=models.EmailField()

    

