<<<<<<< HEAD
from dataclasses import fields
from django.forms import ModelForm
from .models import BloodStock, VaccineStock


=======
from django.forms import ModelForm
from .models import BloodStock, VaccineStock

>>>>>>> cc211a397fdeca62c41250165c08d2b64aa99404
class BloodStockCreateForm(ModelForm):
    class Meta:
        model = BloodStock
        fields = (
<<<<<<< HEAD
            'blood_group' ,
            'count'
        )


=======
            'blood_group',
            'count'
        )

>>>>>>> cc211a397fdeca62c41250165c08d2b64aa99404
class VaccineStockCreateForm(ModelForm):
    class Meta:
        model = VaccineStock
        fields = (
<<<<<<< HEAD
            'vaccine_name' ,
            'count'
        )
=======
            'vaccine_name',
            'count'
        )

        
>>>>>>> cc211a397fdeca62c41250165c08d2b64aa99404
