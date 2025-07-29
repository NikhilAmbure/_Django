from django.urls import path, include
from .views import index, order, order_pizza

urlpatterns = [
    path('', index, name='index'),
    path('<order_id>/', order, name='order'),
    path('order_pizza/<pizza_id>/', order_pizza, name='order_pizza')
]