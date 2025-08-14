from django.db import models
from django.contrib.auth.models import User

# Create your models here.\


class UserExtended(models.Model):
    user = models.OneToOneField(User, related_name='extended', on_delete=models.CASCADE)
    is_vip = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username

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
    


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
