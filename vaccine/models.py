from django.db import models

# Create your models here.

class Vaccines(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class VaccineNeedy(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    place = models.CharField(max_length=50)
    refid = models.BigIntegerField()
    needed_vaccine = models.ForeignKey(Vaccines, on_delete=models.SET_DEFAULT, null=True, default="covishield")

    def __str__(self):
        return self.name

class BloodDonor(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    place = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name