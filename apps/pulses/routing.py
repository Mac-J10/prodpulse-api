from django.urls import re_path
from .consumers import PulseStreamConsumer

websocket_urlpatterns = [
    re_path(r"ws/pulses/stream/$", PulseStreamConsumer.as_asgi()),
]
