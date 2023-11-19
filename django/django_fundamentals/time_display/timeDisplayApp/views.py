from django.shortcuts import render 
from time import gmtime, strftime
# Create your views here.
import datetime

def displaytime(request):
    current_time = datetime.datetime.now()
    context = {
        "time": current_time,
        "time1": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
 
    return render(request,'index.html', context)
    
  


 
# using now() to get current time

 
# Printing value of now.
# print("Time now at greenwich meridian is:", )