from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from DjHNS.settings import LOGIN_REDIRECT_URL
from .forms import DonorRegForm
from .models import BloodDonor
from stocks.models import BloodStock

# Create your views here.

def blood_stock(request):
    blood_stock = BloodStock.objects.all()
    donars = BloodDonor.objects.all()
    groups = {}
    for donar in donars:
        if donar.blood_group in groups.keys():
            groups[donar.blood_group] += 1
        else:
            groups[donar.blood_group] = 1
    return render(request,"bloodbank/blood_stock.html", context={'stock':blood_stock, 'groups' : groups})

@login_required
def bloodbank_about(request):
    return render(request,"bloodbank/bloodbank_about.html")

@login_required
def donor_reg(request):
    form = DonorRegForm()
    if request.method == "POST":
        form = DonorRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        "form": form
    }
    return render(request,"bloodbank/donor_reg.html", context)

