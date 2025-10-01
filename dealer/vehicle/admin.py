from django.contrib import admin
from cms.admin.placeholderadmin import FrontendEditableAdminMixin
from .models import CarType, Car

# Register your models here.

@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Car)
class CarAdmin(FrontendEditableAdminMixin, admin.ModelAdmin):
    frontend_editable_fields = ("name", "color")
