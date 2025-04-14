from itertools import product

from django.db import models
from django.template.defaultfilters import slugify

from home.utils import generateSlug
from django.db.models import CheckConstraint, Q




# Create your models here.

class College(models.Model):
    college_name = models.CharField(max_length=100)
    college_address = models.CharField(max_length=100)

class Student(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, blank=True)
    gender_choices = (('Male','Male'), ('female', 'female'))
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=gender_choices, default='Male')
    age = models.IntegerField(null=True, blank=True)
    # date_of_birth = models.DateField()
    # profile_img = models.ImageField(null=True, blank=True, upload_to="student")
    # file = models.FileField(upload_to="files")
    student_bio = models.TextField()
    # created_at = models.DateTimeField(auto_created=True)
    # updated_at = models.DateTimeField(auto_now_add=True)


# Relationships

# OneToOneField (One to one)
class Author(models.Model):
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name

class Book(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=255)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        db_table = 'book'
        ordering = ('price',)
        verbose_name = "Book"
        verbose_name_plural = "Book"

# Foreign Key (OneToMany)
class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='IN')

    # Dunder str method
    def __str__(self):
        return self.brand_name  
    # Prints like this 
    # <QuerySet [<Brand: Jps>, <Brand: TCS>]>

    class Meta:
        unique_together = ('brand_name', 'country')
        # index_together = ('brand_name', 'country')

class Products(models.Model):
    # brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, null=True)

    # overriding save() method
    def save(self, *args, **kwargs) -> None:
        # print("Called")
        # To generate unique slug for same product name
        if not self.id:
            self.slug = generateSlug(self.product_name, Products)
        return super().save(*args, **kwargs)


# Model Manager + Soft delete implementation
class SkillManager(models.Manager):

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_deleted=False)

# Model Manager + Soft Delete implementation
# ManyToMany
class Skills(models.Model):
    skill_name = models.CharField(max_length=100)

    # Model Manager + soft delete
    is_deleted = models.BooleanField(default=False)

    # It returns only is_deleted=false data i.e not deleted data
    objects = SkillManager()

    # Here, it returns the all data whether it is deleted or not
    new_manager = models.Manager()

    def __str__(self):
        return self.skill_name

class Person(models.Model):
    person_name = models.CharField(max_length=100)
    skill = models.ManyToManyField(Skills)

# Constraints in Meta Classes
class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(upload_to="files/", null=True, blank=True)

    class Meta:
        constraints = [
            CheckConstraint(check=Q(age__gte=18), name='age_gte_18'),
        ]

# Proxy field in meta classes
class CollegeStudent(Student2):
    pass
    # class Meta:
            # proxy = True
            # constraints = [
                # CheckConstraint(check=Q(age__gte=20), name='age_gte_20'),
            # ]


# Permission in Meta
class MyModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        # permissions = ['Can create', 'Can update']
        pass


# Abstract class in Meta class
class Human(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    phone_number = models.CharField(max_length=20)

    class Meta:
        abstract = True

class Engineer(Human):
    technology = models.CharField(max_length=100)

class HR(Human):
    responsibilities = models.TextField()

class Investor(Human):
    Money = models.IntegerField()

