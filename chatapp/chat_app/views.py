from django.shortcuts import render, redirect
from chat_app.models import ChatRoom, Message
from django.http import HttpResponse, JsonResponse, Http404
import logging

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = ChatRoom.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

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
    
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    try:
        room_details = ChatRoom.objects.get(name=room)
    except ChatRoom.DoesNotExist:
        raise Http404("Chat room does not exist")

    message = Message.objects.filter(room = room_details.id).order_by('date')
    return JsonResponse({"message":list(message.values())})