from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'index.html',{'name':'hitesh'});
def check(request):

    res=request.GET["exampleInputEmail1"]
    return render(request,'result.html',{'result':res});
