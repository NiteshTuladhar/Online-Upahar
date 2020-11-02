from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'Profile'

urlpatterns = [
   path('userprofile/',views.userProfile,name='userprofile'),
   path('profilechange/', views.profile_edit, name="profilechange"),
   path('profileuser/',views.completeuserprofile, name='completeuserprofile')
   
]