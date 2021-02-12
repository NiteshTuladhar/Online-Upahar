from django.db import models
from djrichtextfield.models import RichTextField

class AboutUs(models.Model):

	title = models.CharField(max_length=100)
	body = RichTextField()


	def __str__(self):

<<<<<<< HEAD
		return self.title 











































































































class TermsAndConditions(models.Model):
=======
		return self.title

class PrivacyAndPolicy(models.Model):
>>>>>>> aa7ea4b518d2af8acbb78198a9dadceccfc91c92

	title = models.CharField(max_length=100)
	body = RichTextField()

<<<<<<< HEAD

	def __str__(self):

		return self.title 
=======
	
	def __str__(self):

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
