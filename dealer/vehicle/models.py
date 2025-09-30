from django.db import models
from django.shortcuts import reverse

# Create your models here.

class CarType(models.Model):
    brand = models.CharField(max_length=100)

    def __str__(self):
        return f"==> {self.brand}"


class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    car_type = models.ForeignKey(CarType, on_delete=models.CASCADE)

    def absolute_url(self):
        return reverse("vehicle:cardetail", args=[self.pk])
