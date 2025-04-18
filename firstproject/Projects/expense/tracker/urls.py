from django.urls import path
from tracker.views import index, delTransaction

urlpatterns = [
    path('', index, name="index"),
    path('del-Transaction/<uuid>/', delTransaction, name="delTransaction"),
]