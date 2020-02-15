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
  sos=models.TextField(max_length=700,default="none")
  sms=models.TextField(max_length=700,default="none")


  def __str__(self):
    return self.pincode
  
class dnt(models.Model):

  dnt_name=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  contact_number=models.CharField(max_length=15)
  pincode=models.IntegerField()
  sms_sent=models.TextField(max_length=700,default="none")
  sms_received=models.TextField(max_length=700,default="none")


  def __str__(self):
    return self.dnt_name

class dmt(models.Model):

  dnt_name=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  contact_number=models.CharField(max_length=15)
  email=models.CharField(max_length=100)
  pincode=models.IntegerField()
  sms_sent=models.TextField(max_length=700,default="none")
  sms_received=models.TextField(max_length=700,default="none")


  def __str__(self):
    return self.dnt_name    


class Contact_Us(models.Model):
  firstname=models.CharField(max_length=100)
  lastname=models.CharField(max_length=100)
  state=models.CharField(max_length=100)
  subject=models.TextField()

  def __str__(self):
    return self.firstname



