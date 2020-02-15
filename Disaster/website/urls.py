from django.contrib import admin
from django.urls import path,include,re_path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    path('home/', views.home),
    path('userregister/',views.userregister),
    path('dntregister/',views.dntregister),
    path('dmtregister/',views.dmtregister),
    path('userlogin/',views.userlogin),
    path('dntlogin/',views.dntlogin),
    path('dmtlogin/',views.userregister),
    path('userprofile/',views.userprofile),
    path('dntprofile/',views.dntprofile),
    path('dmtprofile/',views.dmtprofile),
    re_path(r'^login/$',LoginView.as_view(template_name='home.html',redirect_field_name='next'),name='login'),

]