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
