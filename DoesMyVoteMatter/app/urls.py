from django.urls import path
from . import views
from .models import District

urlpatterns = [
    path('home/', views.find_district, name='find_district'),
    path('district-details/<int:district_number>/', views.district_details, name='district_details'),
]