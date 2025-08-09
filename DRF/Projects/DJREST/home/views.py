from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import *
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action



# Model ViewSets (Easy for CRUD)
# And 'action' for performing other logic of the application like, sending an email , notification, etc...
class ProductViewset(viewsets.ModelViewSet):
    # All CRUD will be done in following two lines
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # **********************************
    # action (It's an a api => 'products/v2/export_products/' as a route)
    # detail = True -> def export_products(self, req, pk)
    # else detail = False (no 'pk' is passed)
    @action(detail=False, methods=['POST'])
    def export_products(self, request):
        return Response({
            "status": True,
            "message": "file exported",
            "data": {}
        })
    

    # So, route will be like , => 'products/v2/1/send_email_product/' (where, 1 is a pk of an product)
    @action(detail=True, methods=['POST'])
    def send_email_product(self, request, pk):
        print("Email Sent!!!", pk)
        return Response({
            "status": True,
            "message": f"email sent to {pk}",
            "data": {}
        })





# Concrete View Classes (CRUD)
class ProductListCreate(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # By only above u can perform GET, POST, etc. in Postman (no need to write those manually )
    # Buy u can modify those if u want to


# Mixins + GenericAPI View class (CRUD)
# 1) ListModelMixin
# 2) CreateModelMixin
# 3) UpdateModelMixin
# 4) DestroyModelMixin
class StudentModelListView(ListModelMixin, CreateModelMixin, GenericAPIView):

    # You have to mention following two things here:
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Overriding the get() method
    def get_queryset(self):
        return Student.objects.filter(name__startwith = 'N')
    
    # Overriding the create method
    # Gets called automatically when data is created
    def perform_create(self, serializer):
        return super().perform_create(serializer)

    # ListModelMixin
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # CreateModelMixin
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

# APIView
# Overrides the methods -> get, post, patch ,etc...
class StudentAPI(APIView):
    
    def get(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)

        return Response({
            "status": True,
            "message": "All records fetched successfully",
            "data": serializer.data
        })
    
    
    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data = data)

        
        if not serializer.is_valid():
            return Response({
                "status": False,
                "message": "Record not created",
                "errors": serializer.errors
            })
        
        
        serializer.save()

        return Response({
            "status": True, 
            "message": "Record created successfully",
            "data": serializer.data
        })




# Function based view (API)
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
    # serializer = BookSerializer(data = data)

    # For CreateBook or NewBookSerializer
    serializer = NewBookSerializer(data=data)
    # serializer = CreateBookSerializer(data = data)

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
    # serializer = BookSerializer(queryset, many = True)

    # for NewBookSerializer (Author, Publisher, Book)
    serializer = NewBookSerializer(queryset, many = True)

    return Response({
        "status": True, 
        "message": "Record created successfully",
        "data": serializer.data
    })



@api_view(['POST'])
def create_user(request):

    data = request.data
    serializer = UserSerializer(data = data)

    # If False -> Error
    # Basic Data validation (By DRF default validation method )
    if not serializer.is_valid():
        return Response({
            "status": False,
            "message": "Record not created",
            "errors": serializer.errors
        })
    
    print(serializer.validated_data)

    return Response({
        "status": True, 
        "message": "Record created successfully",
        "data": serializer.data
    })