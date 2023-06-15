from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.contrib import auth
from django.shortcuts import redirect, render
# Create your views here.
from django.http import HttpRequest



def userlogin(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']         
        user=auth.authenticate(username=username,password=password)
        request.session["username"]=username
        request.session["password"]=password

        if user is None:
            messages.info(request,'error message')
            return redirect("userlogin")
        else:
            if user.is_staff==False and user.is_superuser==False:
                messages.info(request,'hello', user.username)
                auth.login(request,user)
                print(user)
                return redirect('/',{'user': user})
            else: 
                messages.info(request,'Invalid user')
                print(user)
                return redirect('/',{'user': user})
    return render(request,'userlogin.html');



