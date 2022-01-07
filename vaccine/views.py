from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    #return HttpResponse("Hello World")
    return render(request,"home_page.html")

def vaccine_reg(request):
    return render(request,"vaccine/vaccine_reg.html")
