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

from .forms import CourseForm
from .models import Course
# Create your views here.

class CourseListView(ListView):
	#this template_name overrides the default template name that is built when using class based views
	#which would be appname/modelname_viewname.html 
	template_name = 'courses/course_list.html'
	queryset = Course.objects.all()

class CourseDetailView(DetailView):
	#this is the updated method that allows the int:id url var
	template_name = 'courses/course_detail.html'

	def get_object(self):
		#this overrides pk as the key to the item
		id_ = self.kwargs.get("id")
		return get_object_or_404(Course, id=id_)

class CourseUpdateView(UpdateView):
	#this template_name overrides the default template name that is built when using class based views
	#which would be appname/modelname_viewname.html 
	template_name = 'courses/course_edit.html'
	form_class = CourseForm
	queryset = Course.objects.all()
	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

	def get_object(self):
		#this overrides pk as the key to the item
		id_ = self.kwargs.get("id")
		return get_object_or_404(Course, id=id_)

class CourseCreateView(CreateView):
	#this template_name overrides the default template name that is built when using class based views
	#which would be appname/modelname_viewname.html 
	template_name = 'courses/course_edit.html'
	form_class = CourseForm
	queryset = Course.objects.all()
	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

class CourseDeleteView(DeleteView):
	#this is the updated method that allows the int:id url var
	template_name = 'courses/course_delete.html'
	#queryset = Article.objects.all()

	#success URL is required.  option 1 (or use simple url)
	#def get_success_url(self):
		#return '/articlesnew/'
	#success URL is required.  option 2 using reverse call.  import at top
	def get_success_url(self):
		return reverse('courses:courses-list')

	def get_object(self):
		#this overrides pk as the key to the item
		id_ = self.kwargs.get("id")
		return get_object_or_404(Course, id=id_)

