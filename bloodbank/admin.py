from django.contrib import admin

# Register your models here.

from .models import BloodDonor, BloodGroups

admin.site.register(BloodDonor)
admin.site.register(BloodGroups)