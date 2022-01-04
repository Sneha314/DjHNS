from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    #return HttpResponse("Hello World")
    return render(request,"vaccine/home_page.html")
