from django import forms
from .models import Vaccines, VaccineNeedy

class VaccineRegForm(forms.ModelForm):
    class Meta:
        model = VaccineNeedy
        fields = ['name', 'age', 'place', 'refid', 'needed_vaccine']