from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def root(request):
    dojo = Dojos.objects.all()
    return render(request,"index.html",{'DojoStates' : dojo})

def createDojo(requst):
    Name = requst.POST['name']
    City = requst.POST['city']
    State = requst.POST['state']
    Dojos.objects.create(name = Name,city = City, state =State)
    
    return redirect('/')

def createNinja(request):  
    firstName = request.POST['first_name']
    lastName = request.POST['last_name']
    states = request.POST['state']
    dojoObj =Dojos.objects.get(id=states)
    
    Ninjas.objects.create(first_name=firstName,last_name=lastName,dojo=dojoObj)
   
    return redirect('/')
