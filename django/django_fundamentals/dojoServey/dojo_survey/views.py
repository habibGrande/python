from django.shortcuts import render

# Create your views here.
def root (request):

    return render(request,'index.html' )

def show(request):
    
    name =request.POST['userName']
    location = request.POST['dojoLocations']
    language = request.POST['FavoritetLanguage']
    comment= request.POST['comment']
    Gender=request.POST['Gender']
    vehicle=request.POST['vehicle1']
    context ={
            'show_name' : name,
            'show_Location' : location,
            'show_language' : language,
            'show_comment' : comment,
            'show_Gender': Gender ,
            'show_vehicle': vehicle
        }
    return render(request, 'show.html',context)