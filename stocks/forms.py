from dataclasses import fields
from django.forms import ModelForm
from .models import BloodStock, VaccineStock

class BloodStockCreateForm(ModelForm):
    class Meta:
        model = BloodStock
        fields = (
            'blood_group' ,
            'count'
        )


class VaccineStockCreateForm(ModelForm):
    class Meta:
        model = VaccineStock
        fields = (
            'vaccine_name' ,
            'count'
        )

