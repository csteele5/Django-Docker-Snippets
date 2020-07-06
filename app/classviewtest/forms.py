from django import forms

from .models import Classview

class ClassviewModelForm(forms.ModelForm):
	title 		= forms.CharField(label='', 
								  widget=forms.TextInput(
										attrs={
											"placeholder": "your title",
											"id": "my-id-for-title"
										}
									))
	
	class Meta:
		model = Classview
		fields = [
			'title',
		]
	#original way
	'''
	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		if not "CFE" in title:
			raise forms.ValidationError("This is not a valid title. CFE must be in title.")
		return title
	'''
	#second way
	def clean_title(self):
		title = self.cleaned_data.get("title")
		if not "CFE" in title:
			raise forms.ValidationError("This is not a valid title. CFE must be in title.")
		return title