from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db.models.signals import post_save
from django.template.loader import get_template
from django.core.mail import EmailMessage


business_type = [('Sole Proprietorship','Sole Proprietorship'), ('Partnership','Partnership'), ('Corporation','Corporation'),('Shop','Shop')]

class AccountManager(BaseUserManager):
    def create_user(self, email,account_name,password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            account_name = account_name,
            password = password
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user



class SellerAccount(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    account_name = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    website = models.URLField(max_length=50, null=True)
    date_of_establishment = models.DateField(null=True)
    brand_name = models.CharField(max_length=30, null=True, blank=True)
    business_type = models.CharField(max_length=30,choices=business_type,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    token = models.CharField(max_length=20, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    send_first_email = models.BooleanField(default=False)
    profile_create = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=True)



    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['account_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Contact_Seller_Account(models.Model):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    account_name = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    website = models.URLField(max_length=50, null=True)
    date_of_establishment = models.DateField(null=True)
    business_type = models.CharField(max_length=30,choices=business_type,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    token = models.CharField(max_length=20, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    brand_name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.email



def sendAccountCreationMail(sender, **kwargs):
    current_user = kwargs['instance']
    current_user_mail = current_user.email
    token = current_user.token
    s = "Account Creation"
    context = {
        'id' : current_user.id,
        'name' : current_user.account_name,
        'subject' : s,
        'message' : "Your Account Has Been Created Successfully.",
        'token': token
    }
    temp = get_template('welcomemail.html').render(context)
    email = EmailMessage(

        subject=s, 
        body=temp, 
        to= [current_user_mail]

        )

    email.content_subtype = 'html'

    try:
        if current_user.send_first_email==False:
            email.send()
            current_user.send_first_email=True
            current_user.save()
            
    except:
        pass

post_save.connect(sendAccountCreationMail,sender=SellerAccount)

