from django import forms

from .models import Course

class CourseForm(forms.ModelForm):
	title 		= forms.CharField(label='', 
								  widget=forms.TextInput(
										attrs={
											"placeholder": "your title",
											"id": "my-id-for-title"
										}
									))
	instructor 		= forms.CharField(label='', 
								  widget=forms.TextInput(
										attrs={
											"placeholder": "the instructor",
											"id": "my-id-for-instructor"
										}
									))
	description		= forms.CharField(required=False, 
								  widget=forms.Textarea(
										attrs={
											"placeholder": "your description",
											"class": "new-class-name two",
											"id": "my-id-for-description",
											"rows": 3,
											"cols": 120
										}
									)
								  )
	# active		= forms.BooleanField(required=True, 
	# 							  widget=forms.Textarea(
	# 									attrs={
	# 										"class": "new-class-name two",
	# 										"id": "my-id-for-active"
	# 									}
	# 								)
	# 							  )
	class Meta:
		model = Course
		fields = [
			'title',
			'instructor',
			'description',
			'active',
		]
	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		if not "CFE" in title:
			raise forms.ValidationError("This is not a valid title. CFE must be in title.")
		return title
	
	def clean_instructor(self, *args, **kwargs):
		instructor = self.cleaned_data.get("instructor")
		if not "Sir" in instructor:
			raise forms.ValidationError("This is not a valid instructor. Sir must be in instructor.")
		return instructor
