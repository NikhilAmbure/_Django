from django.db import models

# Signal
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

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