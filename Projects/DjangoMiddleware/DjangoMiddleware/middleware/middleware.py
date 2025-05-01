# To write the IP whitelisting things..


from django.http import HttpResponseForbidden



ALLOWED_IPS = ["123.45.67.89", "987.56.65.21"]



class IPBlockingMiddleware():


    # To grab the IP
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    # First function (Constructor)
    def __init__(self, get_response) -> None:
        self.get_response = get_response
    

    def __call__(self, request):
        ip = self.get_client_ip(request)
        print(ip)
        if ip in ALLOWED_IPS:
            return HttpResponseForbidden("Forbiddnen: IP not allowed")
        
        return self.get_response(request)