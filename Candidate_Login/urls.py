from django.urls import path

from . import views



urlpatterns = [

path('candidateLogin',views.candidateLogin,name='candidateLogin'),

]