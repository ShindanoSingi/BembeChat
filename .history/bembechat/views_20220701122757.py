from ast import Return
from django.shortcuts import render

# import the form from forms.py
from .forms import Forms

# Create your views here.
def welcomePage(request):
    return render(request, 'bembechat/welcome_Page.html')