from django.shortcuts import render
from django.contrib import messages


from travello.models import Destination
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
        
        return render(request,'index.html')

@login_required(login_url="login")
def information(request):
        dests=Destination.objects.all()
        return render(request,'information.html',{'dests':dests})

@login_required(login_url="login")
def payment(request):

        
        return render(request,'payment.html')

@login_required(login_url="login")
def paid(request):

        messages.info(request,'Payment successful !!! ')
        dests=Destination.objects.all()
        
        return render(request,'paid.html',{'dests':dests})


@login_required(login_url="login")
def payform(request):
        return render(request,'payform.html')

def about(request):
        return render(request,'about.html')


