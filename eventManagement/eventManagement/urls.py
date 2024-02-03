"""
URL configuration for eventManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from stellarPass.views import index,about,rentVenue,showsEvents,NeonGrooveArena,rhytmicOasis,ticketdetails,bigwater,wonderland,tiger,havenCourtyard,reservation_view,signup,signin,signout,mycart
from stellarPass.views import ropt,ngpt,hcpt,wpt,bwspt,tdpt,sbpt,event_list, event_detail, ticket_list, purchase_ticket, view_cart



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/',about,name='about'),
    path('rent-venue/',rentVenue,name='rentVenue'),
    path('shows-events/',showsEvents,name='showsEvents'),

    path('mycart/',mycart,name='mycart'),
    path('havenCourtyard/',havenCourtyard,name='havenCourtyard'),

    path('NeonGrooveArena/',NeonGrooveArena,name = 'NeonGrooveArena'),
    path('rhytmicOasis/',rhytmicOasis,name = 'rhytmicOasis'),
    path('ticket-details/',ticketdetails,name='ticket-details'),

    path('bigwater/',bigwater,name='bigwater'),
    path('wonderland/',wonderland,name='wonderland'),
    path('tiger/',tiger,name='tiger'),

    

    path('reservation/', reservation_view, name='reservation_view'),

    
    path('signup/',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('signout/', signout, name='signout'),

    path('ropt/', ropt, name='ropt'),
    path('ngpt/', ngpt, name='ngpt'),
    path('hcpt/', hcpt, name='hcpt'),
    path('wpt/', wpt, name='wpt'),
    path('bwspt/', bwspt, name='bwspt'),
    path('tdpt/', tdpt, name='tdpt'),
    path('sbpt/', sbpt, name='sbpt'),

    path('events/', event_list, name='event_list'),
    path('events/<int:event_id>/', event_detail, name='event_detail'),

    path('tickets/', ticket_list, name='ticket_list'),
    path('purchase_ticket/<int:event_id>/', purchase_ticket, name='purchase_ticket'),

    path('cart/', view_cart, name='view_cart'),
]

