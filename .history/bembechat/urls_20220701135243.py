from unicodedata import name
from django.urls import path


from  . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('signup/', views.signup, name='signup'),
]
