# from turtle import up
from django.contrib.auth.models import User
from django.db import connections, models
from django.urls import reverse

# To check if the other user is online
from django.core.cache import cache
import datetime
from bembechat_django import settings


# from room.views import room

# Room model.
class Room(models.Model):
      name = models.CharField(max_length=255)
      slug = models.SlugField(unique=True)
      username = models.CharField(max_length=255)

      def __str__(self): # new
            return self.slug

      def get_absolute_url(self): # new
            return reverse("room/room_page.html", args=[str(self.slug)])



# Declare fields for online
class Profile(models.Model):
      user = models.OneToOneField(User, related_name='profile', on_delete = models.CASCADE)
      # name = models.CharField(max_length=255, default=None, null=True)
      # room = models.ManyToManyField(Room, related_name='profile')
      # message = models.ManyToManyField(Message, related_name='profile')
      message_color = models.CharField(max_length=255, default='lightblue')
      is_online = models.BooleanField(default=False)
      avatar = models.ImageField(upload_to="images/", blank=True, null=True)

      # def __str__(self):
      #       return self.name

# User model.
class  Message(models.Model):
      room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
      user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
      profile = models.ForeignKey(Profile, related_name='messages', on_delete=models.CASCADE, default=1)
      image = models.ImageField(upload_to="images/", null=True, blank=True)
      content = models.TextField()
      date_added = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return f'{self.user.username}: {self.content} [{self.date_added}]'

      class Meta:
            ordering = ('date_added',)



