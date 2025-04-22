from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.FloatField()
    sku = models.CharField(max_length=100)
    # brand = models.CharField(max_length=100, default=None)
    thumbnail = models.URLField(max_length=1000)

    def __str__(self) -> str:
        return self.title   