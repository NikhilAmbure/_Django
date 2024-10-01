from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('dynamic_route/<int:number>', views.dynamic_route)
]
