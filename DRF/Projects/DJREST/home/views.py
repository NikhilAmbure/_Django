from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student

# Also u can use one api for all the methods following

@api_view(['POST', 'GET', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'])
def index(request):
    students = ["Abhijeet", "Nikhil", "Parle"]
    data = {
        "status": True,
        "message": "This is from django rest framework",
        "students": students,
        "method": f"{request.method}"
    }
    return Response(data)


# Sending data from frontend to backend (Using POSTMAN)
# There is no html form in this case to save and create a record
@api_view(['POST'])
def create_record(request):

    # Printing the data came from the frontend
    # print(request.data)

    # Creating a record in the database without serializer
    data  = request.data
    Student.objects.create(**data)

    return Response({
        "status": True, 
        "message": "Record created successfully"
    })


# Getting all records from the database
@api_view(['GET'])
def get_all_records(request):
    students = [
        {
            "id": student.id,
            "name": student.name,
            "email": student.email, 
            "dob": student.dob,
            "phone": student.phone
        }
        for student in Student.objects.all()
    ]

    return Response({
        "status": True,
        "message": "All records fetched successfully",
        "data": students
    })


@api_view(['DELETE'])
def delete_record(request, id):
    try: 
        student = Student.objects.get(id=id).delete()
    except Exception as e:
        return Response({
            "status": False,
            "message": "Record not found"
        })
    
    return Response({
        "status": True,
        "message": "Record deleted successfully"
    })