from django.contrib import admin
from .models import Order, Pizza
# Register your models here.

admin.site.register(Pizza)
admin.site.register(Order)