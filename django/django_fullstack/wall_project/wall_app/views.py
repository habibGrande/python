import bcrypt
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
# Create your views here.
def root(request):
    users = Users.objects.all()
    context ={
        'user': users
    }
    return render(request,'index.html', context)

def create_user(request):
    errors = Users.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value,extra_tags=key) 
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_pass = request.POST['conf-pass']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        users = Users.objects.create(first_name = first_name, last_name =last_name, email   = email, passowrd = pw_hash , confirm_passowrd = pw_hash)
        print(pw_hash)
        return redirect('/')

def login(request):
    user = Users.objects.get(email=request.POST['email-login'])
    
    if bcrypt.checkpw(request.POST['password-login'].encode(), user.passowrd.encode()):
        users_name = Users.objects.all()
        return render(request,'success.html',users_name)
    else:
        return redirect('/')