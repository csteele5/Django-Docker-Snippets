from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	title 		= forms.CharField(label='', 
								  widget=forms.TextInput(
										attrs={
											"placeholder": "your title",
											"id": "my-id-for-title"
										}
									))
	description	= forms.CharField(required=False, 
								  widget=forms.Textarea(
										attrs={
											"placeholder": "your description",
											"class": "new-class-name two",
											"id": "my-id-for-text-area",
											"rows": 3,
											"cols": 120
										}
									)
								  )
	price		= forms.DecimalField(initial=199.99)
	# email 		= forms.EmailField(label='', 
	# 							  widget=forms.TextInput(
	# 									attrs={
	# 										"placeholder": "your email",
	# 										"id": "my-id-for-email"
	# 									}
	# 								))
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]
	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		if not "CFE" in title:
			raise forms.ValidationError("This is not a valid title. CFE must be in title.")
		return title

	#just an example - email is not in the class, but can be added to the form
	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get("email")
		if not email.endswith("edu"):
			raise forms.ValidationError("This is not a valid email. Must end with edu.")
		return email	

class RawProductForm(forms.Form):
	title 		= forms.CharField(label='', 
								  widget=forms.TextInput(
										attrs={
											"placeholder": "your title",
											"id": "my-id-for-title"
										}
									))
	description	= forms.CharField(required=False, 
								  widget=forms.Textarea(
										attrs={
											"placeholder": "your description",
											"class": "new-class-name two",
											"id": "my-id-for-text-area",
											"rows": 3,
											"cols": 120
										}
									)
								  )
	price		= forms.DecimalField(initial=199.99)