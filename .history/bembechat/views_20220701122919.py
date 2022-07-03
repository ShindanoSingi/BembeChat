from django.contrib import login

from ast import Return
from django.shortcuts import render, redirect

# import the form from forms.py
from .forms import SignupForm

# Create your views here.
def welcomePage(request):
    return render(request, 'bembechat/welcome_Page.html')