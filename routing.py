from django.urls import path
from chatapp.consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/chat/<int:room_id>/', ChatConsumer.as_asgi())
]