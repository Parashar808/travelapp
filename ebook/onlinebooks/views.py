from urllib.robotparser import RequestRate
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'parashar'});

def add(request):
    num1=int(request.GET["val1"])
    num2=int(request.GET["val2"])
    res=num1+num2

    return render(request,"result.html",{'result':res})