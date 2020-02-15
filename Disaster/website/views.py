from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import User_request,dmt,Contact_Us


# Create your views here.

def home(request):
	return render(request,'home.html',{})


def userregister(request):
	if request.method=='POST':
		post=User_request()
		post.user_name=request.POST.get('person_name')
		post.location=request.POST.get('address')
		post.contact_number=request.POST.get('contact_number')
		post.gender=request.POST.get('sex')
		post.pincode=request.POST.get('pincode')
		post.date_of_birth=request.POST.get('date_of_birth')
		post.save()
		return render(request,'home.html',{})

	else:

		return render(request,'userregister.html',{})

def dntregister(request):
	return render(request,'userregister.html',{})


def signin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("user_register")
    else:
        form = UserCreationForm()
    return render(request, 'signin.html', {'form': form})

		


def dmtregister(request):
	if request.method=='POST':
		post=User_request()
		post.dmt_name=request.POST.get('person_name')
		post.location=request.POST.get('address')
		post.contact_number=request.POST.get('contact_number')
		post.email=request.POST.get('email')
		post.pincode=request.POST.get('pincode')
		post.sms_sent=request.POST.get('sms_sent')
		post.sms_received=request.POST.get('sms_received')
		post.save()
		return render(request,'home.html',{})

	else:

		return render(request,'userregister.html',{})

#def userlogin(request):
	#return render(request,'home.html',{})

def dntlogin(request):
	return render(request,'login.html',{})

def dmtlogin(request):
	return render(request,'login.html',{})

def userprofile(request):
	return render(request,'home.html',{})

def dmtprofile(request):
	return render(request,'home.html',{})

def dntprofile(request):
	return render(request,'home.html',{})	


