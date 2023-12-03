import bcrypt
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
# Create your views here.
def root(request):
    return render(request,'index.html')

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
        request.session['id']  = users.id
        print(pw_hash)
        return redirect('/wall')

def wall(request):
    if 'id' in request.session:
        user = Users.objects.get(id = request.session['id'])
        messages = Messages.objects.all()
        comments = Comments.objects.all()
        
        context = {
            'user' :user,
            'messages' : messages,
            'comments': comments,
          
        }
        return render (request,'wall.html',context)
    return redirect('/')

def login(request):
    errors = Users.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value) 
        return redirect('/')
    email = request.POST["email-login"]
    user = Users.objects.filter(email=email)
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password-login'].encode(), logged_user.passowrd.encode()):
            request.session['id'] = logged_user.id
            return redirect('/wall')
    else:
        messages.error(request,"User is not Exist")
    return redirect('/')

def logout(request):
    del request.session['id']
    return redirect("/")

def postMessage(request):
    user_id = int(request.POST['user_id'])
    user_obj = Users.objects.get(id = user_id)
    message = request.POST['messege']
    created_message = Messages.objects.create(user = user_obj,masssege = message)
    id = created_message.id
    user_obj.messages.add(created_message)

    return redirect('/wall')

def comment(request):
    user_id = request.session['id']
    user_obj = Users.objects.get(id = user_id)
    mes_id = request.POST['msg_id']
    mesg_obj = Messages.objects.get(id = mes_id)
    comment = request.POST['comment']
    create_comment = Comments.objects.create(comment = comment, user = user_obj, messages = mesg_obj)
    user_obj.comments.add(create_comment)
    mesg_obj.comment.add(create_comment)

    return redirect('/wall')



