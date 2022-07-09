from django.contrib.auth.models import User
from django.db import models

# To check if the otehr user is online
from django.core.cache import cache
import datetime
from bembechat_django import settings


# from room.views import room

# Room model.
class Room(models.Model):
      name = models.CharField(max_length=255)
      slug = models.SlugField(unique=True)

      # def __str__(self):
      #       return self.name

# User model.
class  Message(models.Model):
      room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
      user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
      content = models.TextField()
      date_added = models.DateTimeField(auto_now_add=True)

      class Meta:
            ordering = ('date_added',)

# Declare fields for online
class UserProfile(models.Model):
       user_profile = models.ForeignKey(User, related_name='profile', on_delete = models.CASCADE)
       is_online = models.BooleanField(default=False)
