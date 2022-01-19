from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm

# Create your views here.

def registrations(request):
    return render(request,"users/registrations.html")

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
    return render(request, 'users/register.html', context)

