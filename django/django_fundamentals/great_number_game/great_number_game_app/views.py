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
        color ='#009e0f'
    elif input < request.session['randomINT']:
            text = "too low!"
            color = 'red'
    elif input >  request.session['randomINT']:
            text = "too high!"
            color = 'red'
    context = {
        'color' : color,
        'text' : text ,

   }
    print(request.session['randomINT'])
    return render(request,'index.html', context)
   

