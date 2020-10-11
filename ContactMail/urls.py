from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'ContactMail'

urlpatterns = [
   path('', views.contactpage, name='contactpage'),
   path('sendmail/', views.mailsend, name='sendmail')
   
]