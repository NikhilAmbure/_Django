from rest_framework import serializers
from .models import Student, Book
from datetime import datetime


# Model Serializer
class StudentSerializer(serializers.ModelSerializer):
    
    # Connection between the model and the serializer
    class Meta:
        model = Student
        fields = '__all__'

        # Or if u want to exclude only 1 field from model then 
        # it sends all other fields except "phone"
        # exclude = ["phone"]


    # Calculating student's age by dob
    def calculate_age(self, date_of_birth):
        current_date = datetime.now()

        age = current_date.year - date_of_birth.year
        return age

    def to_representation(self, instance):
        # Gives us all the data
        data = super().to_representation(instance)
        data['age'] = self.calculate_age(instance.dob)
        return data
    
    def create(self, validated_data):
        student = Student.objects.create(**validated_data)
        # Adds 5 zeros
        student.student_id = f"STU-{str(student.id).zfill(5)}"
        student.save()
        return student
    
    
    def get_fields(self):
        fields = super().get_fields()
        print(fields)

        # Consider 
        authenticated = True
        if authenticated:
            # Removing the email (when we send data with email, it'll not receive the email)
            fields.pop('email', None)
            fields.pop('phone', None)

        return fields
    
    
    # ****************
    # when you want to customize how incoming data 
    # (e.g., from a POST or PUT request) is validated and converted 
    # into Python-native types that can be used to create or update model instances.
    def to_internal_value(self, data):
        # print(data) # Use POST in postman
        data = super().to_internal_value(data)
        if 'name' in data:
            # It will remove the extra spaces from name
            data['name'] = data['name'].strip().title()
            print(data)

        return super().to_internal_value(data)



# Basic Serializer / custom Method
# No need to write class Meta and its fields (write manually)
class BookSerializer(serializers.Serializer):
    book_title = serializers.CharField(max_length=100)
    book_author = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    TAX_PRICE = 18

    # method for tax calculation
    def calculate_tax_price(self, price):
        return self.TAX_PRICE + price
    
    # ************Custom methods********

    # 1
    # This method gets automatically called 
    # when we call the save method on queryset
    # We can modify this method too
    def to_representation(self, instance):
        return {
            "book_title": instance.book_title,
            "book_author": instance.book_author,
            "price": self.calculate_tax_price(instance.price)
        }

    # 2
    # Manually write the create method, update
    # custom create method (for saving the records)
    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        return book
    
    # 3
    def update(self, instance, validated_data):
        book_title = validated_data.get('book_title', instance.book_title) 
        book_author = validated_data.get('book_author', instance.book_author) 
        price = validated_data.get('price', instance.price) 
        
        instance.book_title = book_title
        instance.book_author = book_author
        instance.price = price
        instance.save()

        return instance