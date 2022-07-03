from unicodedata import name
from django.contrib.auth import views as auth_views
from django.urls import path


from  . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='bembechat/login_page.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
