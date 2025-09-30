from django.contrib import admin
from .models import CarType, Car

# Register your models here.

@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
