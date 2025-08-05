from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import *

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
    # data  = request.data
    # Student.objects.create(**data)


    
    # *********Model Serializer**********
    # Creating a record in the database with serializer

    # Validating the data
    data = request.data
    serializer = StudentSerializer(data = data)

    # If False -> Error
    if not serializer.is_valid():
        return Response({
            "status": False,
            "message": "Record not created",
            "errors": serializer.errors
        })
    
    # else
    serializer.save()

    return Response({
        "status": True, 
        "message": "Record created successfully",
        "data": serializer.data
    })



@api_view(['PATCH'])
def update_record(request):

    data = request.data
    if data.get('id') is None:
        return Response({
            "status": False,
            "message": "ID is required for update"
        })

    try:
        # Student_object that we want to update 
        student_obj = Student.objects.get(id = data.get('id'))
        # Partial=True -> Indicates we want to update the data
        serializer = StudentSerializer(student_obj, data = data, partial = True)
        
        # Validate the data before saving
        if not serializer.is_valid():
            return Response({
                "status": False,
                "message": "Record not updated",
                "errors": serializer.errors
            })
        
        serializer.save()
        
        return Response({
            "status": True, 
            "message": "Record updated!",
            "data": serializer.data
        })
    except Student.DoesNotExist:
        return Response({
            "status": False,
            "message": "Student not found"
        })

# Getting all records from the database
@api_view(['GET'])
def get_all_records(request):


    # students = [
    #     {
    #         "id": student.id,
    #         "name": student.name,
    #         "email": student.email, 
    #         "dob": student.dob,
    #         "phone": student.phone
    #     }
    #     for student in Student.objects.all()
    # ]


    # **********Serializer************** (No dependency Or coupling)
     # When we dont want any field from a model so we can just simply remove that field from serializer 
    # instead of clearling out per line of getting a data (like this-> Student.objects.get("phone"))
    # It will take more time but using serializer it will get rapidly fixed

    # ***********ModelSerializer is used here*********

    # A) For only one record
    # Fetch it by ".../?id=" 
    if request.GET.get('id'):
        student = Student.objects.get(id = request.GET.get('id'))
        serializer = StudentSerializer(student)
        return Response({
        "status": True,
        "message": "All records fetched successfully",
        "data": serializer.data
    })

    # B) For multiple records
    # Instead of for loop we can use serializer
    queryset = Student.objects.all()
    # -> many=True" if there are multiple records in queryset
    serializer = StudentSerializer(queryset, many=True)

    return Response({
        "status": True,
        "message": "All records fetched successfully",
        "data": serializer.data
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


# Custom serializer
@api_view(['POST'])
def create_book(request):

    data = request.data
    serializer = BookSerializer(data = data)

    # If False -> Error
    if not serializer.is_valid():
        return Response({
            "status": False,
            "message": "Record not created",
            "errors": serializer.errors
        })
    
    print(serializer.validated_data )

    # Write ur custom save/create method in serializer.py
    serializer.save()

    return Response({
        "status": True, 
        "message": "Record created successfully",
        "data": serializer.data
    })


@api_view(['GET'])
def get_book(request):

    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many = True)

    return Response({
        "status": True, 
        "message": "Record created successfully",
        "data": serializer.data
    })