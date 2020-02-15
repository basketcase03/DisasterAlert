from django.db import models


class User_request(models.Model):
  gender_choices=(
  ("Male","Male"),
  ("Female","Female"),
  ("Other","Other"),
  )

  user_name=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  contact_number=models.CharField(max_length=15)
  gender=models.CharField(max_length=10,choices=gender_choices)
  pincode=models.IntegerField()
  date_of_birth=models.DateField()
  


  def __str__(self):
    return self.user_name

class dmt(models.Model):

  dmt_name=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  contact_number=models.CharField(max_length=15)
  email=models.CharField(max_length=100)
  pincode=models.IntegerField()
  dmt_account_sid=models.CharField(max_length=100,null=True)
  dmt_auth_token=models.CharField(max_length=100,null=True)
  


  def __str__(self):
    return self.dnt_name    

class dnt(models.Model):

  dnt_name=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  contact_number=models.CharField(max_length=15)
  email=models.CharField(max_length=100)
  pincode=models.IntegerField()
  dnt_account_sid=models.CharField(max_length=100,null=True)
  dnt_auth_token=models.CharField(max_length=100,null=True)
  


  def __str__(self):
    return self.dnt_name  


class Contact_Us(models.Model):
  firstname=models.CharField(max_length=100)
  lastname=models.CharField(max_length=100)
  state=models.CharField(max_length=100)
  subject=models.TextField()

  def __str__(self):
    return self.firstname



