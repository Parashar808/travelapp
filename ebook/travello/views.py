from django.shortcuts import render

from travello.models import Destination
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
        dests=Destination.objects.all()
        return render(request,'index.html',{'dests':dests});

@login_required(login_url="login")
def information(request):
        dests=Destination.objects.all()
        return render(request,'information.html',{'dests':dests})

