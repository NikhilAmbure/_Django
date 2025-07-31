from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def index(request):
    students = ["Abhijeet", "Nikhil", "Parle"]
    data = {
        "status": True,
        "message": "This is from django rest framework",
        "students": students,
        "method": f"{request.method}"
    }
    return Response(data)