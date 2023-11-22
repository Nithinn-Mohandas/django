from django.db import models


# Create your models here.

# fname,sname,usrname,email,phn,gender,addres,dob,passw,conf-pass

class register(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    gender = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    dob = models.DateField()
    password = models.CharField(max_length=30)


# file upload ?

class upload(models.Model):
    filename = models.CharField(max_length=30)
    upload = models.FileField(upload_to='django_app/static')
    description = models.CharField(max_length=50)


# employee registration

class employee_registraion(models.Model):
    employeename = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    companyname = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)


# work - product details

class product(models.Model):
    productname = models.CharField(max_length=30)
    price = models.IntegerField()
    companyname = models.CharField(max_length=30)
    quantity = models.IntegerField()
    expiredate = models.DateField()
    description = models.CharField(max_length=30)


# work 2 - files

class uploads(models.Model):
    audioname = models.CharField(max_length=30)
    audioupload = models.FileField(upload_to='django_app/static')
    videoname = models.CharField(max_length=30)
    videoupload = models.FileField(upload_to='django_app/static')
    pdfname = models.CharField(max_length=30)
    pdfupload = models.FileField(upload_to='django_app/static')


# work - fullname,state,language

class check_model(models.Model):
    choice = [
        ('Kerala', 'Kerala'),
        ('Tamilnadu', 'Tamilnadu'),
        ('Karnataka', 'Karnataka')
    ]
    fullname = models.CharField(max_length=30)
    state = models.CharField(max_length=30, choices=choice)
    english = models.BooleanField(default=False)
    malayalam = models.BooleanField(default=False)
    hindi = models.BooleanField(default=False)
