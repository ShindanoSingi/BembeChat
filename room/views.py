from hashlib import new
from unicodedata import name
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from zmq import Message
from .models import Room, Message
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import RoomForm

# Ensure the user is logged in before showing the room list.
@login_required
def rooms(request):
      rooms = Room.objects.all()

      return render(request, 'room/rooms_page.html', {'rooms': rooms})


@login_required
def room(request, slug):
      room = Room.objects.get(slug=slug)

      messages = Message.objects.filter(room=room).order_by('date_added')

      return render(request, 'room/room_page.html', {'room': room, 'messages': messages})

# CREATE a Room
class RoomCreate(CreateView):
      model = Room
      # fields = ['name', 'slug']
      # fields = '__all__'
      form_class = RoomForm
      template_name = 'room/room_form.html'
      success_url = '/rooms/'

# Update a room
class RoomUpdate(UpdateView):
    model = Room
    fields = '__all__'
    template_name = 'room/room_update_form.html'
    success_url = '/rooms/'

# Update a room
class RoomDelete(DeleteView):
    model = Room
    template_name = 'room/room_delete_form.html'
    success_url = '/'


# # Update the message
# class MessageUpdate(UpdateView):
#       model = Message
#       fields = '__all__'
#       template_name = 'room/message_update_form.html'
#       success_url = '/rooms/'