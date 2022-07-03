from django.db import models

# Model for the room.
class Room(models.Model):
      name = models.CharField(max_length=255)
      slug = models.SlugField(unique=True)