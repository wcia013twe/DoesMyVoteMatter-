from django.contrib import admin
from .models import District  # Import the District model

@admin.register(District)  # Decorator to register the model
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'area', 'perimeter', 'congress', 'party')
    search_fields = ('name', 'district', 'congress')  # Allows search functionality
