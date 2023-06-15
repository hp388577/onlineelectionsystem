from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
# Create your views here.

# Create your views here.

def candidateLogin(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']  
        user=User.objects.filter(username=username)
        for u in user:
            if u.is_staff==True and u.is_superuser==False:
                user=auth.authenticate(username=username,password=password)
                auth.login(request,user)
                if user is None:
                    messages.info(request,'you are not valid user')
                    return redirect("candidateLogin")
                else: 
                    messages.info(request,'hello ',user.username)
                    print(user)
                    return redirect('/',{'user': user})
            else:
                messages.info(request,'You are not a valid user')
                return redirect("candidateLogin")
    return render(request,'candidatelogin.html',);
 