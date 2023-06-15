from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Election
from Candidate_Login.models import Candidate
def vote(request):
    username = request.session["username"]
    password = request.session["password"]
    if username and password:
        user = auth.authenticate(username=username, password=password)





def home(request):

    return render(request,'election_create.html');

def election_details(request):
    candidate=Candidate.objects.filter()
    print(candidate)
    election_data=Election.objects.filter()
    return render(request,'election_info.html',{'election_data':election_data,'candidate':candidate})