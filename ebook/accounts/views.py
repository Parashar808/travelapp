from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    
    if request.method== 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user name taken')
                return redirect('/')            
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('/')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('/')


        
    return render(request,'register.html')

def login(request):
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect("information") 

            else:
                messages.info(request,'Invalid ')
                return redirect('login')

        else:
         return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')



# @login_required(login_url="login")
# def information(request):
#     return render(request,'information.html')
