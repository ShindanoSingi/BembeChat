from django.urls import path

from . import views

# The urls below refer to the path in bembe_django/urls.py
urlpatterns = [
      path('', views.rooms, name='rooms'),
      path('new/', views.RoomCreate.as_view(), name='roomNew'),
      path('<slug:slug>/update', views.RoomUpdate.as_view(), name='room_update'),
      path('<slug:slug>/delete', views.RoomDelete.as_view(), name='room_delete'),
      path('messages/<int:pk>/delete', views.MessageDelete.as_view(), name='message_delete'),
      path('<slug:slug>/', views.room, name='room'),


]