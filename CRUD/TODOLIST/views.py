from django.shortcuts import render, redirect                   

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from TODOLIST.models import Complain
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from .forms import ComplainForm


# Create your views here.

# @login_required(login_url="login")

@login_required(login_url="login")
def show_comp(request):
    complains = Complain.objects.all()
    # solutions= Sclass.objects.all()
    return render(request,'show.html',{'complains':complains} )

# @login_required(login_url="login")


# @login_required(login_url="login")
def remove_comp(request, pk):
    Complains = Complain.objects.get(id=pk)

    if request.method == 'POST':
        Complains.delete()
        return redirect('/')

    context = {
        'complains': Complains
    }

    return render(request, 'delete.html', context)


def home(request):

    if 'search' in request.GET:
        search1=request.GET['search']
        complains= Complain.objects.filter(Name__icontains=search1)
    else:
        complains = Complain.objects.all()

    # complains = Complain.objects.all()

    return render(request, 'home.html',{'complains':complains})





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
                return redirect("show/") 

            else:
                messages.info(request,'Invalid ')
                return redirect('login')

        else:
         return render(request,'login.html')
    
# @login_required(login_url="login")
def logout(request):
    auth.logout(request)
    return redirect('/')


# def solution(request, pk):
#     return render(request, 'solutionpage.html')

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['baralpara4@gmail.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("/")
      
	form = ContactForm()
	return render(request, "contact.html", {'form':form})

# @login_required(login_url="login")
def create(request):
    form=ComplainForm()
    if request.method == 'POST':
        form=ComplainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context1={'form':form}
    return render(request,'create.html',context1)

# @login_required(login_url="login")
def update(request, pk):
    comp=Complain.objects.get(id=pk)
    form=ComplainForm(instance=comp)
    if request.method == 'POST':
        form=ComplainForm(request.POST,instance=comp)
        if form.is_valid():
            form.save()
            return redirect("/")


    context1={'form':form}
    return render(request,'create.html',context1)


