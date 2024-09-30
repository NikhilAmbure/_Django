from django.shortcuts import render # type: ignore
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello Client !!')

def contact(request):
    return HttpResponse('Contact me.')