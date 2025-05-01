from django.shortcuts import render
from django.http import JsonResponse

# JsonResponse converts the dictionary data into json type and return it


def index(request):
    
    # Data like following :
    # convert it into json
    data = {
        "status" : True,
        "message" : "django server"
    }

    return JsonResponse(data)
    # It returns the data but if u add the local host ip into middleware.py -> ALLOWED_IPS it will return forbidden