from django.shortcuts import render
import random 	
# Create your views here.
def root(request):
    randomINT = random.randint(1, 100) 
    request.session['randomINT'] = randomINT
    return render(request,'index.html')

def answers(request):
    input =  int(request.POST['number'])
    
    if input == request.session['randomINT']:
        text = f"{request.session['randomINT']} was the number"
        color ='gold'
    elif input < request.session['randomINT']:
            text = f"{input} too low!"
            color = 'red'
    elif input >  request.session['randomINT']:
            text = f"{input} too high!"
            color = 'red'
    context = {
        'color' : color,
        'text' : text ,

   }
    return render(request,'index.html', context)
   

