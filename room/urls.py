from django.urls import path

from . import views

# The urls below refers to the path in bembe_django/urls.py
urlpatterns = [
      path('', views.rooms, name='rooms'),
      path('<slug:slug>/', views.room, name='room'),
]