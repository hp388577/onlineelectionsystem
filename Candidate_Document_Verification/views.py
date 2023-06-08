from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html', {'name': 'hitesh'})

def check(request):
    if request.method == 'POST':
        result = request.POST["exampleInputEmail1"] # Use parentheses instead of square brackets

        return render(request, "result.html", {"result": result})
    else:
        return render(request, 'index.html', {'name': 'hitesh'})
