from django.db import models


# Create your models here.
from django.db import models


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

    def _str_(self):
        return self.name,self.email
    
class newsletterSubscribe(models.Model):
    email = models.EmailField()

    def _str_(self):
        return self.email
    


class SortEvents(models.Model):
    MONTH_CHOICES = [
        ('November', 'November'),
        ('December', 'December'),
        ('January', 'January'),
        ('February', 'February'),
    ]

    LOCATION_CHOICES = [
        ('Lavasa, Pune', 'Lavasa, Pune'),
        ('Mumbai', 'Mumbai'),
        ('Delhi', 'Delhi'),
        ('Bengaluru', 'Bengaluru'),
    ]

    PRICE_CHOICES = [
        ('Rs 1500', 'Rs 1500'),
        ('Rs 3000', 'Rs 3000'),
        ('Rs 5000', 'Rs 5000'),
    ]

    selected_month = models.CharField(max_length=20, choices=MONTH_CHOICES, default='month')
    selected_location = models.CharField(max_length=20, choices=LOCATION_CHOICES, default='location')
    selected_price = models.CharField(max_length=20, choices=PRICE_CHOICES, default='price')
