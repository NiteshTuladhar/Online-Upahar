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

<<<<<<< HEAD
	#title3 = 
	 
	
	#title3_3ontent = 
=======
		return self.title
<<<<<<< HEAD

class Banner(models.Model):
	
	offer = models.CharField(max_length=100)
	title = models.CharField(max_length=200)
	body = RichTextField()
	profile_image = models.ImageField(upload_to='banner_front',blank=True,null=True)

	def __str__(self):

		return self.title
=======
>>>>>>> aa7ea4b518d2af8acbb78198a9dadceccfc91c92
>>>>>>> 876dddf79c8934409473126b77dcca306e41366e
>>>>>>> f0feb739b040b23b62eeae1fa78567581e8242fb
