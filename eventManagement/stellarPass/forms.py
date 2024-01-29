# forms.py
from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'name',
            'email',
            'phone_number',
            'company_organization',
            'venue_requested',
            'type_event',
            'date_requested_first',
            'date_requested_second',
            'about_event_hosting',
        ]

    def __init__(self, *args, **kwargs): 
        super(ReservationForm, self).__init__(*args, **kwargs)
