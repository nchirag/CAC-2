from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import Reservation,Event,Ticket,Cart

# Create your views here.

## FOR DIFFERENT PAGES
def index(request):
    return render(request, 'stellarPass/index.html');

def about(request):
    return render(request, 'stellarPass/about.html');

def rentVenue(request):
    return render(request,'stellarPass/rent-venue.html');

def showsEvents(request):
    return render(request,'stellarPass/shows-events.html');

def mycart(request):
    return render(request,'stellarPass/mycart.html');

def havenCourtyard(request):
    return render(request,'stellarPass/havenCourtyard.html');

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


## FOR SIGN UP

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        myuser = User.objects.create_user(username, email, password)
        myuser.name = username

        myuser.save()

        messages.success(request, "Signed up successfully!!")

        return redirect('signin')

    return render(request,"stellarPass/signup.html");


## FOR SIGN IN

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!") 
            return render(request, "stellarPass/index.html")
            # return redirect('stellarPass/index.html') 
            # username = user.username
            # return render(request, "stellarPass/index.html")

        else:
            messages.error(request, "Incorrect name or password!")
            return redirect('index')



    return render(request,"stellarPass/signin.html");

## FOR SIGN OUT 

def signout(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect('index')



## FOR TABLES:

# reservation table- 

def reservation_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        company_organization = request.POST['company_organization']
        venue_requested = request.POST['venue_requested']
        type_event = request.POST['type_event']
        date_requested_first = request.POST['date_requested_first']
        date_requested_second = request.POST['date_requested_second']
        about_event_hosting = request.POST['about_event_hosting']

        val = Reservation.objects.create(name=name, email=email, phone_number=phone_number, company_organization=company_organization, venue_requested=venue_requested, type_event=type_event, date_requested_first=date_requested_first, date_requested_second=date_requested_second, about_event_hosting=about_event_hosting)
        val.save()
        return render(request, 'stellarPass/rent-venue.html')
    return render(request, 'stellarPass/rent-venue.html')


# event table

def event_list(request):
    events = Event.objects.all()
    return render(request, 'stellarPass/show-events.html', {'events': events})

def event_detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, 'stellarPass/shows-events.html', {'event': event})

# ticket table

def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'stellarPass/mycart.html', {'tickets': tickets})

def purchase_ticket(request, event_id):
    # Assume you have logic to create a ticket and associate it with the current user
    # Adjust this based on your application's requirements
    ticket = Ticket.objects.create(event_id=event_id, user=request.user, price=10.0)
    return render(request, 'stellarPass/mycart.html', {'ticket': ticket})

# cart table

def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'stellarPass/mycart.html', {'cart': cart})


## FOR ACCESS:

@login_required(login_url='/signup')
def ropt(request):
    return render(request,'stellarpass/rhytmicOasis.html')

@login_required(login_url='/signup')
def ngpt(request):
    return render(request,'stellarpass/NeonGrooveArena.html')

@login_required(login_url='/signup')
def hcpt(request):
    return render(request,'stellarpass/havenCourtyard.html')

@login_required(login_url='/signup')
def wpt(request):
    return render(request,'stellarpass/wonderland.html')

@login_required(login_url='/signup')
def bwspt(request):
    return render(request,'stellarpass/bigwatersplash.html')

@login_required(login_url='/signup')
def tdpt(request):
    return render(request,'stellarpass/tigerdancehipop.html')

@login_required(login_url='/signup')
def sbpt(request):
    return render(request,'stellarpass/ticket-details.html')