from django.db import models

# Create your models here.
class User_Data(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=10)
    email=models.EmailField(max_length=25)
    mobile=models.CharField(max_length=10)
    message=models.CharField(max_length=200)