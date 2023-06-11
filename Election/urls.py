from django.urls import path

from . import views



urlpatterns = [

path('election',views.home,name='index'),
path('check',views.result,name='result')
]