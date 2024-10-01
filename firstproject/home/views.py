from django.shortcuts import render # type: ignore
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def dynamic_route(request, number):
    return HttpResponse(f"Dynamic route by number {number}")