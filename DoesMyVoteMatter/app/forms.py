from django import forms
from .models import State  # Import the State model

class DistrictForm(forms.Form):
    state = forms.ModelChoiceField(queryset=State.objects.all(), label="Select a state")
    district_number = forms.IntegerField(label="Enter District Number", min_value=1)
