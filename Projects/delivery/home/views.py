from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')    


def get_data(request):
    latest_data = LocationUpdate.objects.latest('timestpamp')
    return JsonResponse({
        'latitude': latest_data.latitude,
        'longitude': latest_data.longitude, 
        'timestpamp': latest_data.timestpamp
    })