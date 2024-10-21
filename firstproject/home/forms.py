from django import forms 

class StudentForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    # phone_no = forms.CharField()
    # dob = forms.DateField()
    # fathers_name = forms.CharField()