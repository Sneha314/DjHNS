from tokenize import group
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import VaccineRegForm
from .models import VaccineNeedy
from stocks.models import VaccineStock
from django.contrib.auth.decorators import login_required

# Create your views here.

def vaccine_stock(request):
    vaccine_stock = VaccineStock.objects.all()
    needys = VaccineNeedy.objects.all()
    groups = {}
    for needy in needys:
        if needy.needed_vaccine in groups.keys():
            groups[needy.needed_vaccine] += 1
        else:
            groups[needy.needed_vaccine] = 1

    return render(request,"vaccine/vaccine_stock.html", context={'stock':vaccine_stock, 'groups' : groups})

@login_required
def vaccine_about(request):
    return render(request,"vaccine/vaccine_about.html")

@login_required
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
 
