from django.urls import path

from . import views



urlpatterns = [

path('candidatelogin',views.home,name='index')
]