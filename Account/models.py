from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db.models.signals import post_save
from django.template.loader import get_template
from django.core.mail import EmailMessage


gender_list = [('Male','male'),('Female','female'),('Other','other')]

class AccountManager(BaseUserManager):
    def create_user(self, email, date_of_birth,country,image,address,gender,contact_no, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            country=country,
            image=image,
            address=address,
            gender=gender,
            contact_no=contact_no
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,address,gender,contact_no, password=None):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=None ,
            country=None,
            image=None,
            address=address,
            gender=gender,
            contact_no=contact_no
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
    account_name = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(blank=True,null=True,)
    country = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='user/',blank=True,null=True, default='user/unknown.jpg')
    address = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=30,choices=gender_list, null=True, blank=True)
    contact_no = models.CharField(max_length=15, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    token = models.CharField(max_length=20, blank=True, null=True)
    is_verified = models.BooleanField(default=False)



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


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


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
        email.send()
            
    except:
        pass

post_save.connect(sendAccountCreationMail,sender=Account)

