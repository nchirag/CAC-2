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