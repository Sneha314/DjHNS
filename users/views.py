from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def registrations(request):
    return render(request,"users/registrations.html")

