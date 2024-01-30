from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout


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


def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        myuser = User.objects.create_user(username, email, password)
        myuser.name = username

        myuser.save()

        messages.success(request, "Signed up successfully!!!")

        return redirect('signin')

    return render(request,"stellarPass/signup.html");

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

def signout(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect('index')

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
