from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from .models import User_request,dmt,Contact_Us,dnt
from twilio.rest import Client
from django.shortcuts import get_object_or_404


# Create your views here.

def home(request):
	return render(request,'home.html',{})


def send_sms_dnt(request):
	if request.method=='POST':
		area=request.POST.get('pincode')
		num=request.user.id
		userr=dnt.objects.get(dnt_id=num)
		account_sid=userr.dnt_account_sid
		auth_token=userr.dnt_auth_token
		my_twilio=userr.contact_number
		my_msg=request.POST.get('SMS_send')

		client=Client(account_sid,auth_token)
		numbers=User_request.objects.filter(pincode=area)
		for to_num in numbers:
			client.messages.create(to=to_num.contact_number,from_=my_twilio,body=my_msg)
			"""add +91 to phone num. and my_twilio only twilio number"""


		return render(request,'home.html',{})

	else:

		return render(request,'dnt_send_sms.html',{})


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
	if request.method=='POST':
		post=dnt()
		post.dnt_name=request.POST.get('person_name')
		post.location=request.POST.get('address')
		post.contact_number=request.POST.get('contact_number')
		post.email=request.POST.get('email')
		post.pincode=request.POST.get('pincode')
		post.dnt_account_sid=request.POST.get('account_sid')
		post.dnt_auth_token=request.POST.get('auth_token')
		num=request.user.id
		post.dnt_id=num
		post.save()
		return redirect('dnt_sms')

	else:

		return render(request,'dntregister.html',{})


def signin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("dnt_register")
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
		return render(request,'dnt_send_sms.html',{})

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


