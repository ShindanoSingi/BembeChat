from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Room

# Ensure the user is logged in before showing the room list.
@login_required 
def rooms(request):
      rooms = Room.objects.all()
      
      return render(request, 'room/rooms_page.html', {'rooms': rooms})


@login_required 
def room(request, slug):
      room = Room.objects.get(slug=slug)
      
      return render(request, 'room/room.html', {'room': room})