from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import DistrictForm
from .models import District, State
from .math import calculate_efficiencygap, Schwartzberg, polsby_Popper, reock

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
    eg = calculate_efficiencygap(district.democratic_votes, district.republican_votes)
    swhartzberg = Schwartzberg(district.area, district.perimeter)
    polsby = polsby_Popper(district.area, district.perimeter) 
    reock_value = reock(district.area, district.perimeter)
    average_compactness = round((swhartzberg + polsby + reock_value) / 3, 5)
    
    
    context = {
        'state': state ,
        'district': district,
        'efficiency_gap': eg,
        'schwartzberg': swhartzberg,
        'polsby': polsby,
        'reock': reock_value,
        'average' : average_compactness,
    }

    return render(request, 'app/district_details.html', context)
