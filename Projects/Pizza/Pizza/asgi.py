"""
ASGI config for Pizza project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from home.consumer import OrderProgress
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pizza.settings')

application = get_asgi_application()


ws_pattern = [
    path("ws/pizza/<order_id>/", OrderProgress),
]



application = ProtocolTypeRouter({
    # WebSocket chat handler
    "websocket": ((
            URLRouter(ws_pattern)
        )
    ),
})
