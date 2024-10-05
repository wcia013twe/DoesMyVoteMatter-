from django.contrib import admin
from .models import District, State  # Import the District model

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'area', 'perimeter', 'congress', 'party') #Just us telling it what to display on the admin panel when selecting which district

admin.site.register(State)
admin.site.register(District, DistrictAdmin)