"""
URL configuration for onlineelectionsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('Candidate_Document_Verification.urls')),
    path('adminlogin/', include('Admin_Login.urls')),
    path('adminprofile/', include('Admin_Profile.urls')), 
    path('candidatedetails/', include('Candidate_Details.urls')),
    path('candidatelogin', include('Candidate_Login.urls')),
    path('election/', include('Election.urls')),
    path('userlogin', include('User_Login.urls')),
    path('userprofile/', include('User_Profile.urls')),
    path('admin/', admin.site.urls),
]
