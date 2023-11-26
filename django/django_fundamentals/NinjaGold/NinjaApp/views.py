from django.shortcuts import render , redirect
import random
# Create your views here.
def root (request): 
    yourgold = 0
    counter = request.session['yourgold']
    if counter:
        yourgold += counter
    else:
        yourgold = 0
    context ={
        'yourGold' : yourgold
    }
    
    print(yourgold)
    return render(request,'index.html',context)

def process_money(request):
    counter = 0
    gold = 0
    if request.POST['hiddenValue']== 'farm':
        farmNumber =  random.randint(10,20)
        gold += farmNumber

    elif  request.POST['hiddenValue'] == 'cave':
        caveNumber = random.randint(10,20)
        gold += caveNumber

    elif request.POST['hiddenValue'] == "house" :
        houseNumber = random.randint(10,20)
        gold += houseNumber

    elif request.POST['hiddenValue'] == 'quest':
        questNumber = random.randint(10,20)
        gold += questNumber
    
    request.session['yourgold'] = gold

    return  redirect ('/')

# def farm(request):
#     request.session['farmCount'] = random.randint(10,20)
#     farmSession = request.session['farmCount'] 
#     return redirect(process_money)

# def cave(request):
#     request.session['CaveCount'] = random.randint(10,20)
#     caveession = request.session['CaveCount']
#     print(caveession)
#     return redirect(process_money)

# def house(request):
#     request.session['HouseCount'] = random.randint(10,20)
#     houseSession = request.session['HouseCount']
#     print(houseSession)
#     return redirect(process_money)

# def quest(request):
#     request.session['QuestCount'] = random.randint(-50,50)
#     QestSession = request.session['QuestCount']
#     print(QestSession)
#     return redirect(process_money)


# if farmSession < caveession and farmSession < houseSession and farmSession < QestSession:
    #     status = 'farm'
    #     text = f"You entered a farm and earnd {amount} gold."
    # elif caveession < farmSession and caveession < houseSession and caveession < QestSession:
    #     status = 'cave'
    #     text = f'You entered a cave and earnd {amount} gold.'
    # elif houseSession < farmSession and houseSession < caveession and houseSession < QestSession:
    #     status = 'house' 
    #     text =f'You entered a house and earnd {amount} gold.'
    # elif QestSession < houseSession and QestSession < farmSession and QestSession < houseSession :
    #     status = 'quest'
    #     text = f'You entered a quest and earnd {amount} gold.'

        # farmSession = request.POST['farm'] 
    # caveession = request.POST['cave']
    # houseSession = request.POST['house']
    # QestSession = request.POST['quest']