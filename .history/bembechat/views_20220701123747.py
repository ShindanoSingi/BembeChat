from django.contrib.auth import login

from ast import Return
from django.shortcuts import render, redirect

# import the form from forms.py
from .forms import SignupForm

# Create your views here.
def welcomePage(request):
    return render(request, 'bembechat/welcome_Page.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        # Let django handle request/form validation. If the user's data is valid, add the user to the database.
        if form.is_valid():
            user = form.save()
            
            # Call django buil-in "login" to authenticate the user.
            login(request.user)
            
            return redirect('welcome_Page')