from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.
from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
	)

from .forms import ArticleForm
from .models import Article

class ArticleCreateView(CreateView):
	#this template_name overrides the default template name that is built when using class based views
	#which would be appname/modelname_viewname.html 
	template_name = 'articlesnew/article_edit.html'
	form_class = ArticleForm
	queryset = Article.objects.all()
	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

	#options for overriding success url, which is currently the detail view page
	#simple override
	#success_url = '/'
	#function override	
	#def get_success_url(self):
		#return '/articlesnew/'


class ArticleUpdateView(UpdateView):
	#this template_name overrides the default template name that is built when using class based views
	#which would be appname/modelname_viewname.html 
	template_name = 'articlesnew/article_edit.html'
	form_class = ArticleForm
	queryset = Article.objects.all()
	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

	def get_object(self):
		#this overrides pk as the key to the item
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

	#options for overriding success url, which is currently the detail view page
	#simple override
	#success_url = '/'
	#function override	
	#def get_success_url(self):
		#return '/articlesnew/'

class ArticleListView(ListView):
	#this template_name overrides the default template name that is built when using class based views
	#which would be appname/modelname_viewname.html 
	template_name = 'articlesnew/article_list.html'
	queryset = Article.objects.all()

class ArticleDetailViewOLD(DetailView):
	#this is the default method, requiring a url var of int:pk
	template_name = 'articlesnew/article_detail.html'
	queryset = Article.objects.all()

class ArticleDetailView(DetailView):
	#this is the updated method that allows the int:id url var
	template_name = 'articlesnew/article_detail.html'
	#queryset = Article.objects.all()

	def get_object(self):
		#this overrides pk as the key to the item
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

class ArticleDeleteView(DeleteView):
	#this is the updated method that allows the int:id url var
	template_name = 'articlesnew/article_delete.html'
	#queryset = Article.objects.all()

	#success URL is required.  option 1 (or use simple url)
	#def get_success_url(self):
		#return '/articlesnew/'
	#success URL is required.  option 2 using reverse call.  import at top
	def get_success_url(self):
		return reverse('articlesnew:articlesnew-list')

	def get_object(self):
		#this overrides pk as the key to the item
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)