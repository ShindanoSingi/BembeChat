from ast import Return
from django.shortcuts import render

# Create your views here.
def welcomePage(request):
    return render(request, 'bembechat/base.html')