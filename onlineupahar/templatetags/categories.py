from django import template
from Products.models import *

register = template.Library()

register.simple_tag()
def getcategory():
    return {'category': Category.objects.all()}
