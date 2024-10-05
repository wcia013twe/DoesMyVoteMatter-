from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import DistrictForm
from .models import District

def find_district(request):
    district = None
    if request.method == "POST":
        form = DistrictForm(request.POST)
        if form.is_valid():
            district_number = form.cleaned_data['district_number']
            district = District.objects.filter(district=district_number).first()
            if district is None:
                return render(request, 'error.html', {'message': 'District not found'})
    else:
        form = DistrictForm()
    
    return render(request, 'app/find_district.html', {'form': form, 'district': district})

def district_details(request, district_number):
    district = District.objects.filter(district=district_number).first()
    return render(request, 'district_details.html', {'district': district})

