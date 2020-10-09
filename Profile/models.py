from django.db import models
from Account.models import Account

# Create your models here.
gender_list = [('Male','male'),('Female','female'),('Other','other')]

class Profile(models.Model):

    user = models.OneToOneField(Account,on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    profile_image = models.ImageField(default="images/img1.jpg",upload_to='user_profile_img',blank=True,null=True)
    gender = models.CharField(max_length=30,choices=gender_list)
    location = models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.first_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url