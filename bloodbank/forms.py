from django import forms
from .models import BloodDonor

class DonorRegForm(forms.ModelForm):
    class Meta:
        model = BloodDonor
        fields = ['name', 'age', 'place', 'blood_group']