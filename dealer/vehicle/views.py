from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Car

# Create your views here.

class CarListView(ListView):
    model = Car
    queryset = Car.objects.all()


class CarDetailView(DetailView):
    model = Car
    context_object_name = "car"
