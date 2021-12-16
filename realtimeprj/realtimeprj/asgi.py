"""
ASGI config for realtimeprj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter
from intgrs.routing import ws_urlpatterns


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realtimeprj.settings')

application = ProtocolTypeRouter({
    'http' : get_asgi_application(),
    'websocket' : AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})
