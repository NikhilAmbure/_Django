from django.urls import path, include
from . import views
from home.views import *

urlpatterns = [
    path('', views.index, name='index'),
]