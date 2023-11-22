import json

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView



from .forms import *
from .models import *


# HttpResponse --> it is used in django to get a text response in our webpage
# Create your views here.

def first(request):
    return HttpResponse('My first django page')


def second(request):
    return HttpResponse('My second Django Work')


# render
# render is a function that is used toconnect our function with templates to return user interface layer

def third(request):
    return render(request, '1 first.html')


def work(request):
    return render(request, '2 cristiano.html')


# work-  video audio pdf ?

def work(request):
    return render(request, '3 pdf.html')


# work - create a registration page?

def reg_page(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phonenumber')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        password = request.POST.get('password')
        confirm_pass = request.POST.get('confirmpassword')

        if password == confirm_pass:
            call_model = register(firstname=firstname, lastname=lastname, username=username, email=email,
                                  phone=phone, gender=gender, address=address, dob=dob, password=password)
            call_model.save()
            return HttpResponse('Registration Success')
        else:
            return HttpResponse('Password Incorrect')

    return render(request, '4 reg_pg.html')


# work-create login page?

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         call_model = register.objects.all()
#         for i in call_model:
#             if (i.username == username and i.password == password):
#                 return HttpResponse('LOGIN SUCCESSFUL')
#         else:
#             return HttpResponse('LOGIN FAILED')
#     return render(request, '5 login.html')


# work - create home page?

def home(request):
    return render(request, '6 home.html')


# work - create file upload page

def fileupload(request):
    if request.method == 'POST':
        filename = request.POST.get('filename')
        fileupload = request.FILES.get('fileupload')
        description = request.POST.get('description')

        call_model = upload(filename=filename, upload=fileupload, description=description)
        call_model.save()
        return HttpResponse('File upload success')

    return render(request, '7 fileupload.html')


# work - create employee registration page?

def employee_reg(request):
    if request.method == 'POST':
        employeename = request.POST.get('employeename')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        companyname = request.POST.get('companyname')
        designation = request.POST.get('designation')
        call_model = employee_registraion(employeename=employeename, email=email, phonenumber=phonenumber,
                                          companyname=companyname, designation=designation)
        call_model.save()
        return HttpResponse('Registration Success')
    return render(request, '8 emply_reg.html')


# work - search employee

def search_emply(request):
    if request.method == 'POST':
        employeename = request.POST.get('employeename')
        phone = request.POST.get('phonenumber')
        call_model = employee_registraion.objects.all()
        for i in call_model:
            if (i.employeename == employeename and int(i.phonenumber) == int(phone)):
                return HttpResponse('EMPLOYEE FOUND')
        else:
            return HttpResponse('EMPLOYEE NOT FOUND')
    return render(request, '9 emply_search.html')


# work - product details

def product_details(request):
    if request.method == 'POST':
        productname = request.POST.get('productname')
        price = request.POST.get('price')
        companyname = request.POST.get('companyname')
        quantity = request.POST.get('quantity')
        expiredate = request.POST.get('expiredate')
        description = request.POST.get('description')

        call_model = product(productname=productname, price=price, companyname=companyname,
                             quantity=quantity, expiredate=expiredate, description=description)
        call_model.save()
        return HttpResponse('PRODUCT ADDED SUCCESSFULLY')

    return render(request, '10 product_details.html')


# work - product search

def product_search(request):
    if request.method == 'POST':
        productname = request.POST.get('productname')
        companyname = request.POST.get('companyname')

        call_model = product.objects.all()
        for i in call_model:
            if (i.productname == productname and i.companyname == companyname):
                return HttpResponse('PRODUCT FOUND')
            else:
                return HttpResponse('PRODUCT NOT FOUND')
    return render(request, '11 product_search.html')


# work 2 - fileuplod

def file(request):
    if request.method == 'POST':
        audioname = request.POST.get('audioname')
        audioupload = request.FILES['audioupload']
        videoname = request.POST.get('videoname')
        videoupload = request.FILES['videoupload']
        pdfname = request.POST.get('pdfname')
        pdfupload = request.FILES['pdfupload']

        call_model = uploads(audioname=audioname, audioupload=audioupload, videoname=videoname, videoupload=videoupload,
                             pdfname=pdfname, pdfupload=pdfupload)
        call_model.save()
        return HttpResponse('FILES UPLOADED SUCCESSFULLY')
    return render(request, '12 files.html')


# work - fullname,state,language

def check(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        state = request.POST.get('state')

        malayalam = request.POST.get('malayalam')
        if malayalam == 'on':
            malayalam = True
        else:
            malayalam = False

        english = request.POST.get('english')
        if english == 'on':
            english = True
        else:
            english = False

        hindi = request.POST.get('hindi')
        if hindi == 'on':
            hindi = True
        else:
            hindi = False

        call_model = check_model(fullname=fullname, state=state, malayalam=malayalam, english=english, hindi=hindi)
        call_model.save()
        return HttpResponse('DATA SAVED SUCCESSFULLY')
    return render(request, '13 check.html')


# display function - registration

def display(request):
    a = register.objects.all()
    return render(request, '14 display.html', {'data': a})


# display - employee reg

def display_emp(request):
    a = employee_registraion.objects.all()
    return render(request, '15 display_emp.html', {'data': a})


# display file

def filedisplay(request):
    id = []
    filename = []
    img = []
    descrption = []
    a = upload.objects.all()
    for i in a:
        idd = i.id
        id.append(idd)

        file = i.filename
        filename.append(file)

        image = str(i.upload).split('/')[-1]
        img.append(image)

        dis = i.description
        descrption.append(dis)

    mylist = zip(id, filename, img, descrption)  # [(1,cris,image.jpg,suuuii)(2,messi,image.jpg,lm10)]
    return render(request, '16 fileupload.html', {'data': mylist})


# display - uploads

def dis_uploads(request):
    id = []
    audio = []
    audioupload = []
    video = []
    videoupload = []
    pdf = []
    pdfupload = []

    a = uploads.objects.all()

    for i in a:
        idd = i.id
        id.append(idd)
        audioo = i.audioname
        audio.append(audioo)
        aupload = str(i.audioupload).split('/')[-1]
        audioupload.append(aupload)
        videoo = i.videoname
        video.append(videoo)
        vupload = str(i.videoupload).split('/')[-1]
        videoupload.append(vupload)
        pdff = i.pdfname
        pdf.append(pdff)
        pupload = str(i.pdfupload).split('/')[-1]
        pdfupload.append(pupload)

    mylist = zip(id, audio, audioupload, video, videoupload, pdf, pdfupload)
    return render(request, '17 uploads.html', {'data': mylist})


# update

# edit profile

def update_data(request, id):
    a = register.objects.get(id=id)
    if request.method == 'POST':
        a.firstname = request.POST.get('firstname')
        a.lastname = request.POST.get('lastname')
        a.username = request.POST.get('username')
        a.email = request.POST.get('email')
        a.phone = request.POST.get('phonenumber')
        if str(request.POST.get('gender')) == 'female' or str(request.POST.get('gender')) == 'male' or str(
                request.POST.get('gender')) == 'other':
            a.gender = request.POST.get('gender')
            print(a.gender)
        else:
            a.save()
        a.address = request.POST.get('address')
        if len(str(request.POST.get('dob'))) > 0:
            a.dob = request.POST.get('dob')
        else:
            a.save()
        a.save()
        return redirect(display)  # redirect nu ullil display cheyankan vendei create cheytha function name

    return render(request, '18 edit.html', {'data': a})


# employee update

def update_employ(request, id):
    a = employee_registraion.objects.get(id=id)
    if request.method == 'POST':
        a.employeename = request.POST.get('employeename')
        a.email = request.POST.get('email')
        a.phonenumber = request.POST.get('phonenumber')
        a.companyname = request.POST.get('companyname')
        a.designation = request.POST.get('designation')
        a.save()
        return redirect(display_emp)
    return render(request, '19 employee_edit.html', {'data': a})


# file update

def file_update(request, id):
    a = upload.objects.get(id=id)
    img = str(a.upload).split('/')[-1]

    if request.method == 'POST':
        a.filename = request.POST.get('filename')
        if request.FILES.get('fileupload') == None:
            a.save()
        else:
            a.upload = request.FILES['fileupload']
            a.save()
        a.description = request.POST.get('description')
        a.save()
        return redirect(filedisplay)
    return render(request, '20 file edit.html', {'file': a, 'img': img})


# filess update

def files_update(request, id):
    a = uploads.objects.get(id=id)
    audio = str(a.audioupload).split('/')[-1]
    video = str(a.videoupload).split('/')[-1]
    pdf = str(a.pdfupload).split('/')[-1]
    if request.method == 'POST':
        a.audioname = request.POST.get('audioname')
        if request.FILES.get('audioupload') == None:
            a.save()
        else:
            a.audioupload = request.FILES['audioupload']
            a.save()
        a.videoname = request.POST.get('videoname')
        if request.FILES.get('videoupload') == None:
            a.save()
        else:
            a.audioupload = request.FILES['videoupload']
            a.save()
        a.pdfname = request.POST.get('pdfname')
        if request.FILES.get('pdfupload') == None:
            a.save()
        else:
            a.audioupload = request.FILES['pdfupload']
            a.save()
        a.save()
        return redirect(dis_uploads)
    return render(request, '21 files edit.html', {'file': a, 'audio': audio, 'video': video, 'pdf': pdf})


# DELETE

# delete registration

def reg_delete(request, id):
    a = register.objects.get(id=id)
    a.delete()
    return redirect(display)


# delete employee reg

def emply_delete(request, id):
    a = employee_registraion.objects.get(id=id)
    a.delete()
    return redirect(display_emp)


# delete fileupload

def file_delete(request, id):
    a = upload.objects.get(id=id)
    a.delete()
    return redirect(filedisplay)


# authenticated user registration

def register_auth_user(request):
    if request.method == 'POST':
        a = user_reg(request.POST)
        if a.is_valid():  # is_valid() : it check the validity of the form
            user_name = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')  # cleaned_data : form cleaned data is work all validated fileds
            email = request.POST.get('email')  # are stored it returns a dictnory  validated form input filed and values
            password = request.POST.get('password')
            b = User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name, email=email,
                                         password=password)
            b.save()
            return HttpResponse('authenticated user added')
        else:
            return HttpResponse('user not added')
    else:
        form = user_reg()
        return render(request, '22 auth_user_reg.html', {'form': form})


def reg1_user(request):
    if request.method == 'POST':
        a = user_reg1(request.POST)
        if a.is_valid():
            username = a.cleaned_data['username']
            first_name = a.cleaned_data['first_name']
            last_name = a.cleaned_data['last_name']
            email = a.cleaned_data['email']
            password = a.cleaned_data['password']
            confirmpass = a.cleaned_data['confirmpass']

            if password == confirmpass:
                c = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email
                                             )
                c.set_password(password)

                c.save()
                return HttpResponse('registered')
            else:

                return HttpResponse('password incorrect')
        else:
            return HttpResponse('failed')
    else:
        form = user_reg1()
        return render(request, '23 user-reg1.html', {'form': form})


# auth user login

def reg1_login(request):
    if request.method == 'POST':
        form = user_login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # import authentictae
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponse('login successfully')
            else:
                return HttpResponse('invalid username or password')
        else:
            return HttpResponse('invalid username or password')
    else:

        return render(request, '24 user-login.html')


# *************************************************************************************************************

# 27-10-2023

# API INTO DJANGO PROJECT

def movie_api():
    with open(r"C:\Users\nithi\PycharmProjects\Django\django_work\django_app\movie.json", 'r', encoding='utf8') as f:
        data = json.load(f)
    return data


# movie_api()
# data passing to template

class movie_passing(APIView):
    def get(self, request):
        data = movie_api()
        return render(request, '25 restapi.html', {'data': data})


# FILE UPLOAD

def uploads_api():
    with open(r'C:\Users\nithi\PycharmProjects\Django\django_work\django_app\uploads.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    return data


class upload_passing(APIView):
    def get(self, request):
        data = uploads_api()
        return render(request, '26 uplodsapi.html', {'data': data})
