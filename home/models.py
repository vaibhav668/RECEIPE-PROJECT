from django.db import models
class Student(models.Model):
# Create your models here.
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=18)
    email=models.EmailField(default="c.pokf@1")
    address=models.TextField(null=True,blank=True)
class Car(models.Model):
    car_name=models.CharField(max_length=500)
    speed=models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name