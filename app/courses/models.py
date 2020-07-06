from django.db import models
from django.urls import reverse

# Create your models here.
class Course(models.Model):
	title 		= models.CharField(max_length=120)
	instructor 	= models.CharField(max_length=120) # max_length = required
	description = models.TextField(blank=True, null=True)
	active		= models.BooleanField(default=True)

	def get_absolute_url(self):
		#return f"/products/{self.id}/"  #works, but not dynamic, based on urls.py
		#products:product-detail meash the products namespace as defined in the urls.py
		# THIS IS THE KEY REASON FOR REVERSE - to make this module portal, using reverse and namespaces
		# the class based method uses pk instead of id
		#return reverse("articlesnew:articlesnew-detail", kwargs={"pk":self.id}) 
		return reverse("courses:courses-detail", kwargs={"id":self.id}) 
