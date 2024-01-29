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


def NeonGrooveArena(request):
    return render(request,'stellarPass/NeonGrooveArena.html');

def rhytmicOasis(request):
    return render(request,'stellarpass/rhytmicOasis.html');

def ticketdetails(request):
    return render(request,'stellarPass/ticket-details.html');


def bigwater(request):
    return render(request, 'stellarPass/bigwatersplash.html');

def wonderland(request):
    return render(request, 'stellarPass/wonderland.html');

def tiger(request):
    return render(request, 'stellarPass/tigerdancehipop.html');

