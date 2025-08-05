from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length=100,null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    dob = models.DateField()
    phone = models.CharField(max_length=12)


class Book(models.Model):
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    price = models.IntegerField()
