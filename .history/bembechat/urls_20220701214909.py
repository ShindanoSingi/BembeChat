from unicodedata import name
from.contrib.auth import views as auth_views
from django.urls import path


from  . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('signup/', views.signup, name='signup'),
]
