from django.shortcuts import render, redirect
from chat_app.models import ChatRoom
import logging

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'home.html')

def room(request, room):
    return render(request, 'room.html')

def checkview(request):
    #logger.info("checkview")
    room = request.POST['room_name']
    username = request.POST['username']
    
    if ChatRoom.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = ChatRoom.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
