from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Room

# Ensure the user is logged in before showing the room list.
@login_required 

