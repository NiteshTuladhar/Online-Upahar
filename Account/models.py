from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db.models.signals import post_save
from django.template.loader import get_template
from django.core.mail import EmailMessage
from .token import generatetoken
from SellerAccount.models import SellerAccount



class AccountManager(BaseUserManager):
    def create_user(self, email,account_name=None, username=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            account_name = account_name,
             username=username,
            password=password
           
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,account_name, password=None):
        user = self.create_user(
            email,
            account_name=account_name,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=50, null=True, blank=True)
    account_name = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    token = models.CharField(max_length=20, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    send_first_email = models.BooleanField(default=False)
    profile_create = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)


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





def sendAccountCreationMail(sender, **kwargs):
    current_user = kwargs['instance']
    current_user_mail = current_user.email
    if current_user.token is None:
        current_user.token = generatetoken()
        current_user.profile_create = True
        current_user.save()

        #profile = Profile(user=current_user)
        #profile.save()

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

post_save.connect(sendAccountCreationMail,sender=Account)

