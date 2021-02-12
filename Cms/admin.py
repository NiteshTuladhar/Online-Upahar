from django.contrib import admin
from .models import AboutUs, PrivacyAndPolicy, Banner


# Register your models here.
admin.site.register(AboutUs)
admin.site.register(PrivacyAndPolicy)
admin.site.register(Banner)