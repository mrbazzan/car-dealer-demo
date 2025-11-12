from django.urls import path
from .views import CarListView, CarDetailView

app_name = "vehicle"
urlpatterns = [
    path("", CarListView.as_view(), name="carlist"),
    path("<int:pk>/", CarDetailView.as_view(), name="cardetail"),
]
