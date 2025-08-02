from rest_framework import serializers
from .models import Student



# Model Serializer
class StudentSerializer(serializers.ModelSerializer):
    
    # Connection between the model and the serializer
    class Meta:
        model = Student
        fields = '__all__'

        # Or if u want to exclude only 1 field from model then 
        # it sends all other fields except "phone"
        # exclude = ["phone"]

    