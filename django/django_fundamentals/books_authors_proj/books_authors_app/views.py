from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def root(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request,'index.html',context)

def process(request):
    titles = request.POST['title']
    descs = request.POST['description']
    Book.objects.create(title=titles,desc=descs)
    return redirect ('/')