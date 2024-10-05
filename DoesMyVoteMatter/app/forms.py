from django import forms

class IntegerInputForm(forms.Form):
    integer_value = forms.IntegerField(label="Enter an integer", min_value=0)  # You can set min_value and max_value as needed
