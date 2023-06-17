from django.urls import path

from . import views



urlpatterns = [

path('election',views.home,name='index'),
path('election_details',views.election_details,name='election_details'),
path('vote',views.vote,name='vote'),
path('vote_to_candidate',views.vote_to_candidate,name='vote_to_candidate'),
path('count_votes',views.count_votes,name='count_votes'),



] 