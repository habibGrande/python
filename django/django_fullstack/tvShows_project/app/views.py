from django.shortcuts import render,redirect 
from django.contrib import messages
from .models import *
# Create your views here.

def root(request):
    showAll = Shows.objects.all()
    context ={
      'data' : showAll
    }
    return render (request,'index.html',context)

def new(request):
    return render(request,'create.html')

def create(request):
    errors = Shows.objects.shows_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    elif request.method == 'POST': 
        title = request.POST['title']
        net = request.POST['network']
        date = request.POST['relDate']
        descr = request.POST['desc']
        show=Shows.objects.create(title = title, Network = net, description=descr, Release_Date = date)
        id = show.id
        return redirect(f'/shows/{id}')

def show (request,id):
    show = Shows.objects.get(id=id)
    context ={
        'id' : show.id,
        'title': show.title,
        'network' : show.Network,
        'release_Date' : show.Release_Date,
        'desc' : show.description,
        'updated' :show.updated_at
    }
    return render(request,'show.html',context)

def editPage(request,id):
    show = Shows.objects.get(id=id)
    context ={
        'id' : show.id,
        'title': show.title,
        'network' : show.Network,
        'release_Date' : show.Release_Date,
        'desc' : show.description,
    }
    return render(request,'edit.html',context)

def edit(request,id):
    errors = Shows.objects.shows_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    elif request.method == 'POST': 
        title = request.POST['title']
        net = request.POST['network']
        date = request.POST['relDate']
        descr = request.POST['desc']
        showUpdate = Shows.objects.get(id = id)
        showUpdate.title = title
        showUpdate.Network = net
        showUpdate.Release_Date = date
        showUpdate.description = descr
        showUpdate.save()
        id = showUpdate.id
        return redirect(f'/shows/{id}')

def delete(request,id):
    deleteShow = Shows.objects.get(id = id)
    deleteShow.delete()
    return redirect('/shows')

