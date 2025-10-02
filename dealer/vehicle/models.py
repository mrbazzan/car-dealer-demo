from functools import cached_property

from django.db import models
from django.shortcuts import reverse

from cms.models.fields import PlaceholderRelationField
from cms.utils.placeholder import get_placeholder_from_slot

# Create your models here.

class CarType(models.Model):
    brand = models.CharField(max_length=100)

    def __str__(self):
        return f"==> {self.brand}"


class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    car_type = models.ForeignKey(CarType, on_delete=models.CASCADE)

    placeholders = PlaceholderRelationField()

    @cached_property
    def content(self):
        return get_placeholder_from_slot(self.placeholders, "Page Content")

    def get_template(self):
        return "vehicle/car_detail.html"

    def absolute_url(self):
        return reverse("vehicle:cardetail", args=[self.pk])
