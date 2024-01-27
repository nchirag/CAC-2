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
from stellarPass.views import index,about,rentVenue,showsEvents,tickets,bigwater,wonderland,tiger


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('rent-venue/',rentVenue,name='rentVenue'),
    path('shows-events/',showsEvents,name='showsEvents'),
    path('tickets/',tickets,name='tickets'),
    path('bigwater/',bigwater,name='bigwater'),
    path('wonderland/',wonderland,name='wonderland'),
    path('tiger/',tiger,name='tiger'),
]

