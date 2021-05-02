
from django.urls import path

from django.conf.urls.static import static
from . import views

app_name = 'Api'

urlpatterns = [
   
   path('all_products/',views.AllProductsList.as_view()),

]