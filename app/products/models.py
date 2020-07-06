from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
	title 		= models.CharField(max_length=120) # max_length = required
	description = models.TextField(blank=True, null=True)
	price 		= models.DecimalField(decimal_places=2,max_digits=6) 
	summary 	= models.TextField(blank=False, null=False) 
	featured	= models.BooleanField(default=False)

	def get_absolute_url(self):
		#return f"/products/{self.id}/"  #works, but not dynamic, based on urls.py
		#products:product-detail meash the products namespace as defined in the urls.py
		# THIS IS THE KEY REASON FOR REVERSE - to make this module portal, using reverse and namespaces
		return reverse("products:product-detail", kwargs={"id":self.id}) # this calls the name of the url from the urlpatterns