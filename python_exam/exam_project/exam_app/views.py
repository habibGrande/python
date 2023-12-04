from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt
# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value) 
        return redirect('/')
    fName = request.POST['first_name']
    lName = request.POST['last_name']
    email =  request.POST['email']
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    conPassword = request.POST['confrim_password']
    new_user = User.objects.create(firstName = fName, lastName = lName, email = email, password = pw_hash)
    request.session['id']  = new_user.id
    return redirect('/dashboard')

def dashboard(request):
    if "id" in request.session:
        user = User.objects.get(id = request.session['id'])
        reports = Report.objects.all()
        context = {
            "user" : user,
            'reports' : reports
        }
        return render(request, "dashboard.html", context)
    return redirect('/')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value) 
        return redirect('/')
    email = request.POST["email"]
    password = request.POST['password']
    user = User.objects.filter(email=email)
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['id'] = logged_user.id
            return redirect('/dashboard')
    else:
        messages.error(request,"User is not Exist")
    return redirect('/')

def logout(request):
    del request.session['id']
    return redirect("/")


def report_page(request):
    return render(request,'report.html')

def createReport(request):
    errors = Report.objects.report_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value) 
        return redirect('/new')
    else:  
        location = request.POST['location']
        date = request.POST['SightDate']
        number_sas = request.POST['numberSas']
        desc = request.POST['desc']
        userID = request.session['id']
        user = User.objects.get(id = userID)
        report = Report.objects.create(location = location, date = date,numberOfSasq = number_sas, desc= desc , user = user)
        user.reports.add(report)
        id = report.id
        return redirect('/dashboard')


def editPage(request):
    reportID =  int(request.POST['report'])
    print(reportID)
    report = Report.objects.get(id = reportID)
    context = {
        'report' : report
    }
    return render(request,'edit.html',context)


    
def edit(request):
    errors = Report.objects.report_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value) 
        return redirect('/edits')
    
    else:  
        location = request.POST['location']
        date = request.POST['SightDate']
        number_sas = request.POST['numberSas']
        desc = request.POST['desc']
        userID = request.session['id']
        user = User.objects.get(id = userID)
        report_id = request.POST['report']
        report_update = Report.objects.get(id = report_id)
        report_update.location = location
        report_update.date = date
        report_update.numberOfSasq = number_sas
        report_update.desc= desc
        report_update.save()
       
        return redirect('/dashboard')
    

def delete(request):
    id = request.POST['repor']
    report = Report.objects.get(id = id)
    report.delete()
    return redirect('/dashboard')



def show(request):
    id = request.POST['viewID']
    report = Report.objects.get(id = id)
    context = {
        'report': report
    }
    return render (request,'show.html',context)

    
