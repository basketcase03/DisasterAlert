from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('home/', views.home),
    path('userregister/',view.userregister),
    path('dntregister/',view.dntregister),
    path('dmtregister/',view.dmtregister),
    path('userlogin/',view.userlogin),
    path('dntlogin/',view.dntlogin),
    path('dmtlogin/',view.userregister),
    path('userprofile/',view.userprofile),
    path('dntprofile/',view.dntprofile),
    path('dmtprofile/',view.dmtprofile),

]