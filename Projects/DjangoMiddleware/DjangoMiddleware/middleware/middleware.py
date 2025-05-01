# To write the IP whitelisting things..


from django.http import HttpResponseForbidden
from home.models import Store

ALLOWED_IPS = ["123.45.67.89", "987.56.65.21"]



class IPBlockingMiddleware:

    # First function (Constructor)
    def __init__(self, get_response) -> None:
        self.get_response = get_response


    # To grab the IP
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    # main logic
    def __call__(self, request):
        ip = self.get_client_ip(request)
        print(ip)
        if ip in ALLOWED_IPS:
            return HttpResponseForbidden("Forbiddnen: IP not allowed")
        
        return self.get_response(request)
    

# Middleware for store
class CheckBMPHeader:


    def __init__(self, get_response) -> None:
        self.get_response = get_response


    # main logic
    def __call__(self, request):
        headers = request.headers
        
        if "bmp" not in headers:
            return HttpResponseForbidden("Missing: header bmp")
        else:
            if Store.objects.filter(bmp_id = headers.get('bmp')).exists():
                return HttpResponseForbidden("Invalid: bmp")
        
        return self.get_response(request)