from django.db import models
from djrichtextfield.models import RichTextField

class AboutUs(models.Model):

	title = models.CharField(max_length=100)
	body = RichTextField()


	def __str__(self):

		return self.title 



class TermsAndConditions(models.Model):
	title = models.CharField(max_length=100)
	body = RichTextField()


	def __str__(self):

		return self.title 
		
class PrivacyAndPolicy(models.Model):

	title = models.CharField(max_length=100)
	body = RichTextField()


	def __str__(self):
		return self.title 



class Banner(models.Model):
	
	offer = models.CharField(max_length=100)
	title = models.CharField(max_length=200)
	body = RichTextField()
	profile_image = models.ImageField(upload_to='banner_front',blank=True,null=True)

	def __str__(self):

		return self.title
