from django.shortcuts import render
from home.rabbitmq import publish_message
import random
# Create your views here.


def index(request):
    message = f"This is a demo message - {random.randint(1, 100)}" # Message
    publish_message(message)
    return render(request, 'index.html')