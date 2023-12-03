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
    book = Book.objects.create(title=titles,desc=descs)
    id = book.id
    return redirect ('/')

def show (request,id):
    book = Book.objects.get(id=id)
    authors_of_book = book.author.all()
    all_authors = Author.objects.all()
    print(authors_of_book)
    context ={
        'id' : book.id,
        'title': book.title,
        'desc' : book.desc,
        'authors':authors_of_book,
        'all_authors': all_authors
    }
    return render(request,'books_show.html',context)


def add_author(request,id):
    author_id = request.POST['user']
    author = Author.objects.get(id = author_id)
    book = Book.objects.get(id = id)    
    book.author.add(author)
    return redirect(f'/books/{id}')


def author(request):
    author = Author.objects.all()
    context = {
        'authors': author
    }
    return render(request,'author.html',context)

def Author_process(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    note = request.POST['note']
    author = Author.objects.create(first_name = first_name,last_name = last_name, note= note)
    id = author.id
    return redirect ('/author')

def author_show(request,id):
    author = Author.objects.get(id=id)
    context ={
        'id' : author.id,
        'first_name': author.first_name,
        'last_name' : author.last_name,
        'note': author.note
    }
    return render(request,'author_show.html',context)