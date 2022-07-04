from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from zmq import Message
from .models import Room, Message

# Ensure the user is logged in before showing the room list.
# @login_required 
def rooms(request):
      rooms = Room.objects.all()
      
      return render(request, 'room/rooms_page.html', {'rooms': rooms})


@login_required 
def room(request, slug):
      room = Room.objects.get(slug=slug)
      
      messages = Message.objects.filter(room=room).order_by('date_added')[0:10]
      
      return render(request, 'room/room_page.html', {'room': room, 'messages': messages})