from django.contrib import admin
<<<<<<< HEAD

from .models import AboutUs, PrivacyAndPolicy, Banner,TermsAndConditions
# Register your models here.

=======


from .models import AboutUs, TermsAndConditions, PrivacyAndPolicy, Banner



# Register your models here.

>>>>>>> 16b9d16ff5113de2d04fa151e02cb0d18fad2166
admin.site.register(AboutUs)
admin.site.register(TermsAndConditions)
admin.site.register(PrivacyAndPolicy)
admin.site.register(Banner)
