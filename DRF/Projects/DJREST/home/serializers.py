from rest_framework import serializers
from .models import *
from datetime import datetime
from rest_framework.validators import UniqueValidator
from .validators import no_numbers

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


    # Overrides how an object is serialized to JSON (outbound).
    # This allows complete control over the serialized output.
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
    # -> Use this when you need custom validation or transformation on input data before saving.
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
    # *******UniqueValidator******
    # Same title of the book will not come
    book_title = serializers.CharField(
        max_length=100,
        validators = [
            UniqueValidator(queryset=Book.objects.all())
        ])
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


# For nested serializer(Used this in Userserializer)
class AddressSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=100)
    postal_code = serializers.CharField(max_length=100)

    def validate_postal_code(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Postal_code must contain digits")
        return value
    

# Advance serializer validation
class UserSerializer(serializers.Serializer):
    # Custom validator (validators.py)
    name = serializers.CharField(
        max_length=100,
        validators = [no_numbers] 
        )
    email = serializers.EmailField()
    age = serializers.IntegerField()
    # Generate regex for indian phone_number from gpt 
    # Also, can pass the custom error_messages 
    phone_number = serializers.RegexField(
        regex=r'^(?:\+91[-\s]?|0)?[6-9]\d{9}$',
        error_messages = { 'invalid': 'Phone number be entered correctly'}
    )

    # Nested Serializer
    address = AddressSerializer()
    
    # Dynamic
    user_type = serializers.ChoiceField(choices=['admin', 'regular'])
    admin_code = serializers.CharField(required = False)

    # Instead of writing the separate validation for fields
    # Multiple validation 
    def validate(self, data): 
        print(data)
        if 'age' in data and data['age'] < 18 or data['age'] > 30:
            raise serializers.ValidationError("Age must be greater than 18 and less than 30")

        # Dynamic
        if data['user_type'] == 'admin' and not data.get('admin_code'):
            raise serializers.ValidationError("Admin code is required.")
        
        return super().validate(data)



    # validate_<field_name>:
    # def validate_age(self, value):
    #     if value < 18 or value > 30:
    #         raise serializers.ValidationError("Age must be greater than 18 and less than 30")
    #     return value
    
    # def validate_email(self, value):
    #     if value.split('@')[1] == "gmail.com":
    #         raise serializers.ValidationError("Must be a business email")
    #     return value



# *************Nested Serializer Advance**************
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class NewBookSerializer(serializers.ModelSerializer):

    # It uses foreign key in models
    book_author = AuthorSerializer()

    # ManytoMany field
    publisher = PublisherSerializer(many = True)

    class Meta:
        model = Book
        fields = '__all__'


    # Instead of writing the CreateBookSerializer
    # Override the create method
    def create(self, validated_data):
        author_data = validated_data.pop('book_author')
        publisher_data = validated_data.pop('publisher')

        # creating data
        author, _ = Author.objects.get_or_create(**author_data)
        book = Book.objects.create(book_author=author, **validated_data)
        for pub in publisher_data:
            pub,_ = Publisher.objects.get_or_create(**pub)
            book.publisher.add(pub)
        
        return book
        


class CreateBookSerializer(serializers.ModelSerializer):

    # Takes only valid data
    # And we can use the filter() for getting author by their 'id'
    book_author = serializers.PrimaryKeyRelatedField(queryset = Author.objects.all())
    
    publisher = serializers.PrimaryKeyRelatedField(queryset = Publisher.objects.all(), many=True)

    class Meta:                 
        model = Book
        fields = '__all__'