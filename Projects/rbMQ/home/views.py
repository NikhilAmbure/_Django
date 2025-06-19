from django.shortcuts import render
from home.rabbitmq import publish_message
import random
from faker import Faker
fake = Faker()
# Create your views here.


def index(request):
    message = f"This is a demo message - {random.randint(1, 100)}" # Message
    names = [{
        'name': fake.name(),
        'address': fake.address()
    } for _ in range(10)
    ]

    publish_message(names)
    return render(request, 'index.html')