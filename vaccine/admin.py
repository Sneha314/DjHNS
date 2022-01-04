from django.contrib import admin

# Register your models here.

from .models import Vaccines, VaccineNeedy, BloodDonor

admin.site.register(Vaccines)
admin.site.register(VaccineNeedy)
admin.site.register(BloodDonor)
