from django.db import models

# Create your models here.
#crud
class Student (models.Model):
    # id = models.AutoField()

    name = models.CharField(max_length=100)
    age =models.IntegerField(default=18)
    email=models.EmailField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
   

from django.db import models

class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)

    def __str__(self):
        return f"{self.car_name} - {self.speed} mph"
