from django.urls import path

from . import views



urlpatterns = [
 
path('userlogin',views.userlogin,name='userlogin'),

]