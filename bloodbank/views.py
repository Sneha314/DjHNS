from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blood_stock(request):
    return render(request,"bloodbank/blood_stock.html")

