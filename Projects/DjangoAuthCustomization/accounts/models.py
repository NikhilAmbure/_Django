from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


# Creating custom user model
# By extending the default fields using AbstractUser
class CustomUser(AbstractUser):
    username = None

    phone_number = models.CharField(max_length=12, unique=True)
    image = models.ImageField(upload_to="profile")
    is_verified = models.BooleanField(default=False)

    # To store the otp
    otp = models.IntegerField(default=0)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()
    