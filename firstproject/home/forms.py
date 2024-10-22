from django import forms 
from home.models import *

# class StudentForm(forms.Form):
    # name = forms.CharField()
    # age = forms.IntegerField()
    # phone_no = forms.CharField()
    # dob = forms.DateField()
    # fathers_name = forms.CharField()

# FOrms using models
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ['name', 'age']