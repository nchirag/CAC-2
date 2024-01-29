from django.shortcuts import render, redirect



# Create your views here.

def index(request):
    return render(request, 'stellarPass/index.html');

def about(request):
    return render(request, 'stellarPass/about.html');

def rentVenue(request):
    return render(request,'stellarPass/rent-venue.html');

def showsEvents(request):
    return render(request,'stellarPass/shows-events.html');

def tickets(request):
    return render(request,'stellarPass/tickets.html');

<<<<<<< HEAD
def bigwater(request):
    return render(request, 'stellarPass/bigwatersplash.html');

def wonderland(request):
    return render(request, 'stellarPass/wonderland.html');

def tiger(request):
    return render(request, 'stellarPass/tigerdancehipop.html');
=======
>>>>>>> a2969898fc546ad859f99995c9e2493aad0fe820
