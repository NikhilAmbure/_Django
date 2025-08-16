# Custom throttles
from rest_framework.throttling import BaseThrottle


class CustomThrottle(BaseThrottle):

    # Modify this method
    def allow_request(self, request, view):

        # For, the specific user/ip cannot access this api 
        # (for now here we r using local address)
        if request.META['REMOTE_ADDR'] == "127.0.0.1":
            # return False
            return True
        return True
    