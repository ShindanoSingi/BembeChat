from ast import Return
from django.shortcuts import render

# Create your views here.
def basePage(request):
    return render(request, 'bembechat/welco_PAGE.html')