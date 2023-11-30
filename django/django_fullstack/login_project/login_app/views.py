from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def root(request):
    users = Users.objects.all()
    context ={
        'user': users
    }
    return render(request,'index.html', context)

def create_user(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    confirm_pass = request.POST['conf-pass']
    users = users.objects.create(first_name = first_name, last_name =last_name, email   = email, password = password, confirm_passowrd = confirm_pass)
    return redirect('/')