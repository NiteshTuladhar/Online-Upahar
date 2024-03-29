"""onlineupahar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'Account'

urlpatterns = [
   path('login/',views.userLogin,name='login'),
   path('register/',views.userRegister,name='register'),
   path('logout/', views.userlogout, name='logout'),
   path('account-verify/<int:id>/<str:token>/',views.verifyaccount,name='verify_token'),
   path('verification-page/', views.verifypage, name='verifypage'),
]
