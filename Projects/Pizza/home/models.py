from django.db import models
from django.contrib.auth.models import User
import random
import string
# Create your models here.


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.URLField()


    def __str__(self) -> str:
        return self.name
    


class Order(models.Model):
    STATUS = (("Order Recieved", "Order Recieved"),
              ("Baking", "Baking"),
              ("Baked", "Baked"),
              ("Out of delivery", "Out of delivery"),
              ("Order Delivered", "Order Delivered")
        )
    
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100, null=True, blank=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=100, choices=STATUS, default="Order Recieved")
    created_at = models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.pizza} Status - {self.status}"


    def generateOrderId(self):
        res = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
        return res
    
    
    # Overriding the save method
    def save(self, *args, **kwargs):
        if not self.pk:
            self.order_id = self.generateOrderId()
        
        super(Order, self).save(*args, **kwargs)