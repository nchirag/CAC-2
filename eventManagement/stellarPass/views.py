from django.shortcuts import render, redirect
from .forms import ReservationForm



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
def havenCourtyard(request):
    return render(request,'stellarPass/havenCourtyard.html');

def tigerdancehipop(request):
    return render(request,'stellarPass/tigerdancehipop.html');


=======

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

<<<<<<< HEAD
def login(request):
    return render(request, "stellarPass/log-sign.html");
=======
def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            # Add any additional logic you need after a successful form submission
            return redirect('success_page')  # Redirect to a success page
    else:
        form = ReservationForm()

    return render(request, 'reservation_form.html', {'form': form})
>>>>>>> origin/main

>>>>>>> 396490621594091933729b50ff204143330a7525
