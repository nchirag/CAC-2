from django.shortcuts import render, redirect



# Create your views here.

def index(request):
    return render(request, 'stellarPass/index.html');

def about(request):
    return render(request, 'stellarPass/about.html');