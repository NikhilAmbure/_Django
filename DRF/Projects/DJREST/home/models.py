from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length=100,null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    dob = models.DateField()
    phone = models.CharField(max_length=12)


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name

class Book(models.Model):
    # unique = True -> for UniqueValidator
    book_title = models.CharField(max_length=100, unique=True)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="book_publisher", null=True, blank=True)
    publisher = models.ManyToManyField(Publisher, related_name="books")

    def __str__(self):
        return self.book_title