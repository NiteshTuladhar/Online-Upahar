from django.db import models
from Account.models import Account
from Profile.models import Profile
from Products.models import Product


class Review(models.Model):

    user                = models.ForeignKey(Account,on_delete=models.CASCADE,null=True,blank=True)
    profile             = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    product             = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    message             = models.TextField()
    reply               = models.ForeignKey('Review', null=True, related_name='replies',on_delete=models.CASCADE,blank=True)
    is_approved         = models.BooleanField(default=False)
    comment_time        = models.DateTimeField(auto_now_add=True)


    def __srt__(self):
        return format(self.gigs.title)


    def get_date(self):
    	return self.comment_time.date()