from django.contrib import admin
from .models import *

# Register your models here.

class StoreAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 2:
      return False
    else:
      return True 

admin.site.register(SmallBanner,StoreAdmin)
