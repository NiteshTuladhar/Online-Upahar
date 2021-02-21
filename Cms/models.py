from django.db import models
from djrichtextfield.models import RichTextField

class AboutUs(models.Model):

	title = models.CharField(max_length=100)
	body = RichTextField()


	def __str__(self):

<<<<<<< HEAD
		return self.title 



class TermsAndConditions(models.Model):
	title = models.CharField(max_length=100)
	body = RichTextField()


	def __str__(self):

		return self.title 
		
class PrivacyAndPolicy(models.Model):

	title = models.CharField(max_length=100)
	body = RichTextField()
=======

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

>>>>>>> 16b9d16ff5113de2d04fa151e02cb0d18fad2166



<<<<<<< HEAD
		return self.title 


=======

>>>>>>> 16b9d16ff5113de2d04fa151e02cb0d18fad2166

class Banner(models.Model):
	
	offer = models.CharField(max_length=100)
	title = models.CharField(max_length=200)
	body = RichTextField()
	profile_image = models.ImageField(upload_to='banner_front',blank=True,null=True)

	def __str__(self):

		return self.title
