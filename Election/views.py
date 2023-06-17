from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Election,Vote
from Candidate_Login.models import Candidate

from User_Login.models import UserProfile
from django.db import IntegrityError

def vote(request):
    username = request.session["username"]
    password = request.session["password"]
    if username and password:
        user = auth.authenticate(username=username, password=password)
        userprofile=UserProfile.objects.all()
        userprofile=UserProfile.objects.filter(user=user.id)
        for voter in userprofile:
            if voter.eligible_to_vote==True:
                candidate=Candidate.objects.filter(area_name=voter.area)
                print(candidate)
                election_data=Election.objects.filter()
              

                return render(request,'votenow.html',{'election_data':election_data,'candidate':candidate,'voter':userprofile})
                
    return render(request,'election_info.html')



def home(request):

    return render(request,'election_create.html');

def election_details(request):
    candidate=Candidate.objects.filter()
    print(candidate)
    election_data=Election.objects.filter()
    return render(request,'election_info.html',{'election_data':election_data,'candidate':candidate})


def vote_to_candidate(request):
    try:
        # Get all candidates
        candidates = Candidate.objects.all()
        username = request.session["username"]
        password = request.session["password"]
        if username and password:
            user = auth.authenticate(username=username, password=password)
            userprofile=UserProfile.objects.all()
            userprofile = UserProfile.objects.filter(user=user.id).first()
        for candidate in candidates:
            # Get the candidate's area name
            candidate_area_name = candidate.area_name

            # Get elections with the same area name
            elections = Election.objects.filter(area__name=candidate_area_name)

            for election in elections:
                # Create a vote instance for each election and candidate combination
                vote = Vote.objects.create(
                    voter=request.user.userprofile,  # Assuming the authenticated user has a userprofile
                    election=election,
                    candidate=candidate
                )

                # Save the vote instance
                vote.save()

        return render(request, 'index.html')
    except IntegrityError:
            messages.info(request,{"You have already voted in this election." }  )
            return render(request, 'index.html', {'error_message': messages})
    

from datetime import datetime

from datetime import datetime

def count_votes(request):
    current_datetime = datetime.now()
    current_date = current_datetime.date()

    elections = Election.objects.filter(election_result_date__lte=current_date)

    election_results = {}

    for election in elections:
        votes = Vote.objects.filter(election=election)
        for vote in votes:
            candidate = vote.candidate
            if candidate in election_results:
                election_results[candidate] += 1
            else:
                election_results[candidate] = 1
    print(election_results)
    return render(request, 'result1.html', {'election_results': election_results})

    
    """
vote_to=Vote.objects.filter()
    username = request.session["username"]
    password = request.session["password"]
    if username and password:
        user = auth.authenticate(username=username, password=password)
        userprofile=UserProfile.objects.all()
        userprofile = UserProfile.objects.filter(user=user.id).first()
    candidates = Candidate.objects.filter(area_name=userprofile.area)

    vote_to = Vote.objects.filter(voter=userprofile)
    
    for v in vote_to:
        v.candidate=candidates.first()
        v.voter=userprofile
        v.election=
    return render(request,'index.html')"""
