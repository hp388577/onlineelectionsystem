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
from django.contrib.staticfiles.views import serve


from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('users', include('accounts.urls')),
    path('', include('Admin_Login.urls')),
    path('', include('Candidate_Login.urls')),
    path('', include('Election.urls')),
    path('', include('User_Login.urls')),
    
    path('admin/', admin.site.urls),
    path('static/<path:path>', serve, {'document_root': r'C:\Users\hp388\Projects\onlineelectionsystem\static\css'}),

]
