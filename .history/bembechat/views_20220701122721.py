from ast import Return
from django.shortcuts import render

# im

# Create your views here.
def welcomePage(request):
    return render(request, 'bembechat/welcome_Page.html')