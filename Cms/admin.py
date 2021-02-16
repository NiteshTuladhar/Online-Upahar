from django.contrib import admin


from .models import AboutUs, TermsAndConditions, PrivacyAndPolicy, Banner



# Register your models here.

admin.site.register(AboutUs)
admin.site.register(TermsAndConditions)
admin.site.register(PrivacyAndPolicy)
admin.site.register(Banner)
