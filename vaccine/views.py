from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import VaccineRegForm
from .models import VaccineNeedy

# Create your views here.

def vaccine_stock(request):
    return render(request,"vaccine/vaccine_stock.html")

def vaccine_about(request):
    return render(request,"vaccine/vaccine_about.html")


def vaccine_reg(request):
    form = VaccineRegForm()
    if request.method == "POST":
        form = VaccineRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        "form": form
    }
    return render(request,"vaccine/vaccine_reg.html", context)
 
