from django.urls import path
from tracker.views import index, delTransaction, registration, LoginPage, LogoutPage

urlpatterns = [
    path('', index, name="index"),
    path('registration/', registration, name='registration'),
    path('login/', LoginPage, name="login"),
    path('logout/', LogoutPage, name="logout"),
    path('del-Transaction/<uuid>/', delTransaction, name="delTransaction"),
    
]