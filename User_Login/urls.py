from django.urls import path

from . import views



urlpatterns = [

path('userlogin',views.userlogin,name='index'),
path('profile_create',views.profile_create,name='index'),

]