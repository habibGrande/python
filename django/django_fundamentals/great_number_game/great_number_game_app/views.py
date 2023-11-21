from django.shortcuts import render
import random 	
# Create your views here.
def root(request):
    randomINT = random.randint(1, 100) 
    request.session['randomINT'] = randomINT
    return render(request,'index.html')

def answers(request):
    randomInt =  request.session['randomINT']
    randomIntAsInt = int(randomInt)
    divColor = ''
    user_input = request.POST['number']
    user_inputInt = int(user_input)
    if user_inputInt:
        if user_inputInt == randomIntAsInt:
            divColor = 'gold'
        elif user_inputInt < randomIntAsInt:
            divColor ='red'
        elif user_inputInt > randomIntAsInt:
            divColor = 'red_low'

    print(user_input)
    print(divColor)

    context= {
        'status' : divColor,
        'user_input' : user_inputInt,
        'random_int' : randomIntAsInt
    }
    print(randomInt)
    return render(request,'index.html', context)
   

