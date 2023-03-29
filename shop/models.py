from django.db import models

#Create your models here.
class Car(models.Model):
    marka=models.CharField(max_length=250)
    price=models.CharField(max_length=250)
