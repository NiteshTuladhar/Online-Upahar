from django.db import models
import Account
# Create your models here.
gender_list = [('Male','male'),('Female','female'),('Other','other')]

class Profile(models.Model):

    user = models.OneToOneField(Account.models.Account,on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    profile_image = models.ImageField(default="images/img1.jpg",upload_to='user_profile_img',blank=True,null=True)
    gender = models.CharField(max_length=30,choices=gender_list, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    last_logged_in = models.CharField(max_length=100, null=True)



    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.user.email



class SellerProfile(models.Model):

    user = models.OneToOneField(Account.models.Account,on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    profile_image = models.ImageField(default="images/img1.jpg",upload_to='user_profile_img',blank=True,null=True)
    gender = models.CharField(max_length=30,choices=gender_list, null=True, blank=True)
    shop_name = models.CharField(max_length=30, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)



    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url