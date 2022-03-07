from django.db import models
<<<<<<< HEAD
from bloodbank.models import BloodGroup
=======
from bloodbank.models import BloodGroups
>>>>>>> cc211a397fdeca62c41250165c08d2b64aa99404
from vaccine.models import Vaccines
# Create your models here.

class BloodStock(models.Model):
<<<<<<< HEAD
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
=======
    blood_group = models.ForeignKey(BloodGroups, on_delete=models.CASCADE)
>>>>>>> cc211a397fdeca62c41250165c08d2b64aa99404
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.blood_group}({self.count})'

class VaccineStock(models.Model):
    vaccine_name = models.ForeignKey(Vaccines, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

<<<<<<< HEAD

    def __str__(self):
        return f'{self.vaccine_name}({self.count})'
=======
    def __str__(self):
        return f'{self.vaccine_name}({self.count})'

>>>>>>> cc211a397fdeca62c41250165c08d2b64aa99404
