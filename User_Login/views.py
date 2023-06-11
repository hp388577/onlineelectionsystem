from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def userlogin(request):

    return render(request,'userlogin.html');

def profile_create(request):
    
    return render(request,'userlogin.html');

