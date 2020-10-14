from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 2 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)


class SmallBanner(models.Model):

    banner_name = models.CharField(max_length=50)
    banner_image = models.ImageField(null=True, upload_to ='banner/')
    heading = models.CharField(max_length=15,null=True,blank=True)
    title = models.CharField(max_length=50, null=True,blank=True)
    sub_title = models.CharField(max_length=50, null=True,blank=True)
    button_text = models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return self.banner_name

    def clean(self):
        validate_only_one_instance(self)