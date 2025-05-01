from django.shortcuts import render
from django.http import JsonResponse
from .models import Store

# JsonResponse converts the dictionary data into json type and return it


def index(request):
    
    # print(request.headers.get('bmp'))

    store = Store.objects.get(bmp_id = (request.headers.get('bmp')))

    # Data like following :
    # convert it into json
    data = {
        "status" : True,
        "message" : "store data",
        "data": {
            "bmp_id": store.bmp_id,
            "store_name": store.store_name
        }
    }

    return JsonResponse(data)
    # It returns the data but if u add the local host ip into middleware.py -> ALLOWED_IPS it will return forbidden

