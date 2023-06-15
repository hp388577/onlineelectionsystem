from django.urls import path

from . import views



urlpatterns = [

path('registration',views.registration,name='registration'),
path('participantRegister',views.participantRegister,name='participantRegister'),
path('registration_as_voter',views.registration_as_voter,name='registration_as_voter'),
path('validateToken',views.validateToken,name='validateToken'),
path('registration_as_candidate',views.registration_as_candidate,name='registration_as_candidate'),

path('logout',views.logout,name='logout'),
path('login',views.login,name='login'),
path('',views.home,name='index')

]