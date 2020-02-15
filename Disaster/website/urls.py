from django.contrib import admin
from django.urls import path,include,re_path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    path('home/', views.home,name="home"),
    path('userregister/',views.userregister,name="userregister"),
    path('dnt_send_sms/',views.send_sms_dnt,name="dnt_sms"),
    path('dntregister/',views.dntregister,name="dnt_register"),
    path('dmtregister/',views.dmtregister,name="dmt_register"),
   # path('userlogin/',views.userlogin),
    path('sign_in/',views.signin,name='sign_in'),
    path('dntlogin/',views.dntlogin,name="dnt_login"),
    path('dmtlogin/',views.userregister,name="dmt_login"),
    path('userprofile/',views.userprofile,name="userprofile"),
    path('dntprofile/',views.dntprofile,name="dmt_profile"),
    path('dmtprofile/',views.dmtprofile,name="dnt_profile"),
    re_path(r'^login/$',LoginView.as_view(template_name='login.html',redirect_field_name='next'),name='login'),
    re_path(r'^logout/$',LogoutView.as_view(next_page="home"),name='logout'),

]