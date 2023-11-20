from django.shortcuts import render , redirect

# Create your views here.
def root (request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    return render(request,'index.html' ) 

def destroy(request):
    del request.session['count']
    return redirect ('/')

def incremantByTwo (request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 2
    return render(request,'index.html' ) 