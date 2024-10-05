from django.shortcuts import render # type: ignore
from django.http import HttpResponse

# Create your views here.

def index(request):
    names = ['Fruit', 'Apple', 'ABC']
    context = {
        "names": names,
        "fruits": None,
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def dynamic_route(request, number):
    return HttpResponse(f"Dynamic route by number {number}")