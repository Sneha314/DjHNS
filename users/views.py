from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from bloodbank.models import BloodDonor

from vaccine.models import VaccineNeedy
from .forms import CreateUserForm

# Create your views here.

def registrations(request):
    return render(request,"users/registrations.html")

def vaccine_needys(request):
    vaccine_needys = VaccineNeedy.objects.all()
    context = {
        'vaccine_needys': vaccine_needys
    }
    return render(request,"users/vaccine_needys.html", context)

def blood_donors(request):
    blood_donors = BloodDonor.objects.all()
    context = {
        'blood_donors': blood_donors
    }
    return render(request,"users/blood_donors.html", context)

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form = CreateUserForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)

