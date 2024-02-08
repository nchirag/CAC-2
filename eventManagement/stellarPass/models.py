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
        return self.name,self.email


## NEWSLETTER TABLE  
class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    

