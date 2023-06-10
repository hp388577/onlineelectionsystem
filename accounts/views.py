from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):

    return render(request,'registeration.html');

def result(request):
    if request.method== 'POST':
        result=request.POST['exampleInputEmail1']
        return render(request, "result.html", {"result": result})