from django.shortcuts import render


# Create your views here.

def home(request):
	return render(request,'home.html',{})


def userregister(request):
	return render(request,'home.html',{})

def dntregister(request):
	return render(request,'home.html',{})

def dmtregister(request):
	return render(request,'home.html',{})

def userlogin(request):
	return render(request,'home.html',{})

def dntlogin(request):
	return render(request,'home.html',{})

def dmtlogin(request):
	return render(request,'home.html',{})

def userprofile(request):
	return render(request,'home.html',{})

def dmtprofile(request):
	return render(request,'home.html',{})

def dntprofile(request):
	return render(request,'home.html',{})	


