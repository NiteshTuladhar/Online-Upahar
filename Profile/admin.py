from django.contrib import admin
from .models import Profile, LastLogged_in

# Register your models here.
admin.site.register(Profile)
admin.site.register(LastLogged_in)