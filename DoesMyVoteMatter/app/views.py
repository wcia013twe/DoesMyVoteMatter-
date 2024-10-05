from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import DistrictForm
from .models import District, State

def find_district(request):
    district = None
    if request.method == "POST":
        form = DistrictForm(request.POST)
        if form.is_valid():
            state = form.cleaned_data['state']
            district_number = form.cleaned_data['district_number']
            # Redirect to the district details view
            return redirect('district_details', state_abbreviation=state.abbreviation, district_number=district_number)
    else:
        form = DistrictForm()
    
    return render(request, 'app/find_district.html', {'form': form, 'district': district})

def district_details(request, state_abbreviation, district_number):
    # Get the state object
    state = get_object_or_404(State, abbreviation=state_abbreviation)
    # Get the district object that belongs to the state and has the district number
    district = get_object_or_404(District, state=state, district=district_number)

    return render(request, 'app/district_details.html', {'district': district})
