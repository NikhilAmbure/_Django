from django.db import models
from django.contrib.auth.models import User
import random
import string
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.URLField()


    def __str__(self) -> str:
        return self.name
    

# Order progress mapper
order_mapper = {
    "Order Recieved": 10,
    "Baking" : 40,
    "Baked": 60,
    "Out of delivery": 80,
    "Order Delivered": 100
}


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


    @staticmethod
    def give_order_details(order_id):
        instance = Order.objects.get(order_id=order_id)
        return {
            "order_id": instance.order_id,
            "amount": instance.amount,
            "status": instance.status,
            "date": str(instance.created_at),
            "progress_percentage": order_mapper[instance.status]
        }
    

# Signal for sending the real-time updated data to frontend
@receiver(post_save, sender=Order)
def order_status_handler(sender, instance, created, **kwargs):

    # When order status is updated
    if not created:
        channel_layer = get_channel_layer()
        data = {
            "order_id": instance.order_id,
            "amount": instance.amount,
            "status": instance.status,
            "date": str(instance.created_at),
            "progress_percentage": order_mapper[instance.status]
        }

        # ***************************************
        # sending above data to frontend
        # Now we want to send the data to their correct order_id group
        # Every order_id has its own room/group

        # Why asyntosync -> sends the requests in queue(Redis)
        async_to_sync(channel_layer.group_send)(
            f'order_{instance.order_id}',{
                "type": "order_status",
                'value': json.dumps(data)
            }
        )