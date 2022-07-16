import json
from os import sync

import django

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from django.contrib.auth.models import User

from .models import Room, Message, Profile

class ChatConsumer(AsyncWebsocketConsumer):
      async def connect(self):
            self.room_name = self.scope['url_route']['kwargs']['room_name']
            self.room_group_name = 'chat_%s' % self.room_name

            await self.channel_layer.group_add(
                  self.room_group_name,
                  self.channel_name
            )

            await self.accept()

      async def disconnect(self, event):
            await self.channel_layer.group_discard(
                  self.room_group_name,
                  self.channel_name
                  )

      async def receive(self, text_data):
            data = json.loads(text_data)
            message = data['message']
            username = data['username']
            room = data['room']

            # Save the message before it is sent.
            await self.save_message(username, room, message)


            # Send the messasge to the group
            await self.channel_layer.group_send(
                  self.room_group_name,
                  {
                        'type': 'chat_message',
                        'message': message,
                        'username': username,
                        'room': room,
                  }
            )



      async def chat_message(self, event):

            # Prevent the user from sending empty messages.
            # if(event['message'] == ''):
            #       print('It is empty')
            # else:
            #       print(event['message'])
            #       message = event['message']
            #       username = event['username']
            #       room = event['room']

            # Prevent the user from sending empty messages.
            # if(event['message'] == ''):
            #       print('It is empty')
            # else:
            #       print(event['message'])
            message = event['message']
            username = event['username']
            room = event['room']

            # Send the message to the room so every user in the room can see it.
            await self.send(text_data=json.dumps({
                  'message': message,
                  'username': username,
                  'room': room,
            }))

      @sync_to_async
      def save_message(self, username, room, message):
            user = User.objects.get(username=username)
            room = Room.objects.get(slug=room)

            Message.objects.create(user=user, room=room, content=message)


      @sync_to_async
      def update_user_incr(self, user):
            Profile.objects.filter(pk=user.pk).update(online=True)


      @sync_to_async
      def update_user_decr(self, user):
            Profile.objects.filter(pk=user.pk).update(online=False)
