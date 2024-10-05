from django import forms

class DistrictForm(forms.Form):
    district_number = forms.IntegerField(label="Enter an integer", min_value=1)  # You can set min_value and max_value as needed
