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



#class Footer(models.Model):

	#row1 =
	#row1_content =
	#sub1 = 
	#number = 

	#row2 =
	#r_

	#title3 = 
	 
	
	#title3_3ontent = 