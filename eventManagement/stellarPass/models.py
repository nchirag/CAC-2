from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

## RESERVATION TABLE
class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    company_organization = models.CharField(max_length=50)
    venue_requested = models.CharField(max_length=255)
    type_event = models.CharField(max_length=255)
    date_requested_first = models.DateField()
    date_requested_second = models.DateField()
    about_event_hosting = models.TextField()

    def __str__(self):
        return self.name

## EVENT TABLE    
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    venue = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    # Add other fields as needed

    def __str__(self):
        return self.name
    
## TICKET TABLE
class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # Add other fields as needed

    def __str__(self):
        return f'{self.user.username} - {self.event.name} Ticket'

## CART TABLE
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ticket)
    # Add other fields as needed

    def __str__(self):
        return f'{self.user.username} Cart'
