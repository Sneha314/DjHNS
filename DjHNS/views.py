from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def load_page(request):
    return render(request,"loading.html")

def home_page(request):
    return render(request,"home_page.html")

def stock_management(request):
    return render(request,"stock_management.html")

