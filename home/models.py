from django.db import models

# Create your models here.
class Student (models.Model):
    # id = models.AutoField()

    name = models.CharField(max_length=100)
    age =models.IntegerField(default=18)
    email=models.EmailField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
   

class Product(models.Model):
    pass 