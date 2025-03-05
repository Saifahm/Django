from django.db import models

# Create your models here.
class LoginAdmin(models.Model):
    id=models.CharField(max_length=20,primary_key=True)
    username=models.CharField(max_length=100)
    email=models.CharField (max_length=100)
    password=models.CharField(max_length=100)
    role =models.CharField(max_length=100)
    