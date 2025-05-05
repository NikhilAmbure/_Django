from django.db import models

# Signal
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from PIL import Image
import os

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=(("Male", "Male"), ("Female", "Female")))
    student_id = models.CharField(max_length=10, null=True, blank=True)


# 1) For post_save signal
# When the database gets an entry this function gets called
@receiver(post_save, sender=Student)
def save_student(sender, instance, created, **kwargs):
    print(sender, instance)
    print(created)

    # Created only True when it creates data only at first time after that false
    # Only runs one time here (created)
    if created:
        instance.student_id = f"STU-000{instance.id}"
        instance.save()
        print("Student object created")


# 2) pre_delete signal
@receiver(pre_delete, sender=Student)
def delete_student(sender, instance, **kwargs):
    print("OBJ deleted.")




# ImageResizer via signals
class ImageModel(models.Model):
    original_img = models.ImageField(upload_to="images/", null=True, blank=True)
    thumb_mini = models.ImageField(upload_to="images/thumbnails", null=True, blank=True)
    thumb_small = models.ImageField(upload_to="images/thumbnails", null=True, blank=True)
    thumb_medium = models.ImageField(upload_to="images/thumbnails", null=True, blank=True)
    thumb_large = models.ImageField(upload_to="images/thumbnails", null=True, blank=True)


@receiver(post_save, sender = ImageModel)
def create_thumbnail(sender, instance, created, **kwargs):
    if created:
        sizes = {
            "thumb_mini" : (50, 50),
            "thumb_small" : (100, 100),
            "thumb_medium" : (200, 200),
            "thumb_large" : (400, 400)
        }   

        for fields, size in sizes.items():

            img = Image.open(instance.original_img.path)

            # a high-quality downsampling filter used to resize images.
            img.thumbnail(size, Image.Resampling.LANCZOS)
            
            thumb_name , thumb_extension = os.path.split(instance.original_img.name)
            thumb_extension = thumb_extension.lower()
            thumb_filename = f"{thumb_name}_{size[0]}X{size[1]}{thumb_extension}"
            thumb_path = f"thumbnails/{thumb_filename}"
            img.save(thumb_path)
            setattr(instance, fields, thumb_path)