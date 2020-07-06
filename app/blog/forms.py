from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
	title 		= forms.CharField(label='', 
								  widget=forms.TextInput(
										attrs={
											"placeholder": "your title",
											"id": "my-id-for-title"
										}
									))
	author 		= forms.CharField(label='', 
								  widget=forms.TextInput(
										attrs={
											"placeholder": "the author",
											"id": "my-id-for-author"
										}
									))
	content	= forms.CharField(required=False, 
								  widget=forms.Textarea(
										attrs={
											"placeholder": "your content",
											"class": "new-class-name two",
											"id": "my-id-for-text-area",
											"rows": 3,
											"cols": 120
										}
									)
								  )
	class Meta:
		model = Article
		fields = [
			'title',
			'author',
			'content',
		]
	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		if not "CFE" in title:
			raise forms.ValidationError("This is not a valid title. CFE must be in title.")
		return title
	
	def clean_author(self, *args, **kwargs):
		author = self.cleaned_data.get("author")
		if not "Sir" in author:
			raise forms.ValidationError("This is not a valid author. Sir must be in author.")
		return author
