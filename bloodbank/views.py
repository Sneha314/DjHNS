from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DonorRegForm
from .models import BloodDonor

# Create your views here.

def blood_stock(request):
    return render(request,"bloodbank/blood_stock.html")

def donor_reg(request):
    form = DonorRegForm()
    if request.method == "POST":
        form = DonorRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        "form": form
    }
    return render(request,"bloodbank/donor_reg.html", context)

