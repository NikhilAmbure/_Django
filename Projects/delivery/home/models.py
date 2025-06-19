from django.db import models

# Create your models here.


# To store the latitude and longitude
class LocationUpdate(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestpamp = models.DateTimeField(auto_now_add=True)