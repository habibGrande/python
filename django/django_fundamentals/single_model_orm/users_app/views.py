from django.shortcuts import render , HttpResponse ,redirect
from .models import User
# Create your views here.

def root(request):
    users = User.objects.all()

    context ={
        'users' : users
    }
    return render (request,"index.html", context)

def process(request):
    firstName = request.POST['firstName']
    lastName = request.POST ['LastName']
    email = request.POST['email']
    age = int(request.POST['age'])
    User.objects.create(first_name = firstName,last_name =lastName,email_address = email,age = age)
    return redirect ('/')