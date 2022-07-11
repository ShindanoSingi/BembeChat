from hashlib import new
from unicodedata import name
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from zmq import Message
from .models import Room, Message, Profile
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import RoomForm
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

from django.http import HttpResponse
import datetime

import online_users.models
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save
from datetime import timedelta
from django.contrib.auth.models import User

from django.views.generic import ListView

# Ensure the user is logged in before showing the room list.
@login_required
def rooms(request):
      rooms = Room.objects.all()

      return render(request, 'room/rooms_page.html', {'rooms': rooms})


@login_required
def room(request, slug):
      room = Room.objects.get(slug=slug)
      messages = Message.objects.filter(room=room).order_by('date_added')
      profile = Profile.objects.all()
      return render(request, 'room/room_page.html', {'room': room, 'messages': messages, 'profile': profile})

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#       try:
#             instance.profile.save()
#       except ObjectDoesNotExist:
#             Profile.objects.create(user=instance)

#  Create a profile for the user when a new user is created.
@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
      user = instance
      if created:
            profile = Profile(user=user)
            profile.save()

# Check if the user is already online
@receiver(user_logged_in)
def got_online(sender, user, request, **kwargs):
      user.profile.is_online = True
      user.profile.save()
      # return render(request, 'room/room_page.html', {'user': user})

@receiver(user_logged_out)
def got_offline(sender, user, request, **kwargs):
      user.profile.is_online = False
      user.profile.save()
      # return render(request, 'room/room_page.html', {'user': user})

def see_users(request, self):
      user_status = online_users.models.OnlineUserActivity.get_user_activities(timedelta(seconds=60))
      users = (user for user in  user_status)
      context = {"online_users"}
      # return render(request, 'room/room_page.html', {'user_status': user_status, 'users': users, context: context,})

# Methods for checking if the other user is online or offline.
# @receiver(user_logged_in)
# def got_online(sender, user, request, **kwargs):
#       user.profile.is_online = True
#       user.profile.save()
#       return render(request, 'room/room_page.html', {'user': user, 'is_online': user.profile.is_online})

# @receiver(user_logged_out)
# def got_offline(sender, user, request, **kwargs):
#       user.profile.is_online = False
#       user.profile.save()
#       return render(request, 'room/room_page.html', {'user': user, 'is_online': user.profile.is_online})

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

# View the image from database
class HomePageView(ListView):
    model = Message
    template_name = "room_page.html"


# # Update the message
# class MessageUpdate(UpdateView):
#       model = Message
#       fields = '__all__'
#       template_name = 'room/message_update_form.html'
#       success_url = '/rooms/'


def current_datetime(request):
    now = datetime.datetime.now()
    online = Profile.objects.get(is_online=True)
    html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'room/room_page.html', {'html': html})