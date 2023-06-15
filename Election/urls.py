from django.urls import path

from . import views



urlpatterns = [

path('election',views.home,name='index'),
path('election_details',views.election_details,name='election_details'),
path('vote',views.vote,name='vote'),


] 