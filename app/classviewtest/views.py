from django.shortcuts import render, get_object_or_404, redirect
from django.views	import View

from .forms import ClassviewModelForm
from .models import Classview

#These are the RAW view methods for updating data.  
#The simple class based views accomplish the same things and are much cleaner

#this "mixin" allow simplification of redundant code in the classes.  Extends the below classes
class ClassviewObjectMixin(object):
	model = Classview 

	def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(self.model, id=id)
		return obj

# Create your views here.
class ClassViewDetailView(ClassviewObjectMixin, View):
	template_name = "classview/classview_detail.html"
	def get(self, request, id=None, *args, **kwargs):
		#this line is possible because of mixin
		context = {'object': self.get_object()}
		''' before mixin
		context = {}
		if id is not None:
			obj = get_object_or_404(Classview, id=id)
			context['object'] = obj
		'''	
		return render(request, self.template_name, context)

class ClassViewCreateView(View):
	template_name = "classview/classview_edit.html"
	def get(self, request, *args, **kwargs):
		form = ClassviewModelForm()
		context = {"form": form}
		return render(request, self.template_name, context)
	
	def post(self, request, *args, **kwargs):
		form = ClassviewModelForm(request.POST)
		if form.is_valid():
			form.save()
			print("FORM SAVED")
		else:
			print("FORM NOT SAVED")
		form = ClassviewModelForm()
		context = {"form": form}
		return render(request, self.template_name, context)

class ClassViewUpdateView(ClassviewObjectMixin, View):
	template_name = "classview/classview_edit.html"
	''' replaced through use of ClassviewObjectMixin
	def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(Classview, id=id)
		return obj
	'''

	def get(self, request, id=None, *args, **kwargs):	
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = ClassviewModelForm(instance=obj)
			context['object'] = obj
			context['form'] = form
		return render(request, self.template_name, context)

	def post(self, request, id=None, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = ClassviewModelForm(request.POST,instance=obj)
			if form.is_valid():
				form.save()
				print("Entry Updated: "+obj.title)
			context['object'] = obj
			context['form'] = form
		return render(request, self.template_name, context)

class ClassViewDeleteView(ClassviewObjectMixin, View):
	template_name = "classview/classview_delete.html"
	''' replaced through use of ClassviewObjectMixin
	def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(Classview, id=id)
		return obj
	'''	

	def get(self, request, id=None, *args, **kwargs):	
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = ClassviewModelForm(instance=obj)
			context['object'] = obj
		return render(request, self.template_name, context)

	def post(self, request, id=None, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if obj is not None:
			obj.delete()
			context['object'] = None
			return redirect('/classview/')
		return render(request, self.template_name, context)
		

class ClassViewListView_This_is_one_way_to_do_it(View):
	template_name = "classview/classview_list.html"
	queryset = Classview.objects.all()

	def get(self, request, *args, **kwargs):
		context = {'object_list': self.queryset}
		return render(request, self.template_name, context)

class ClassViewListView(View):
	template_name = "classview/classview_list.html"
	queryset = Classview.objects.all()
	def get_queryset(self):
		return self.queryset

	def get(self, request, *args, **kwargs):
		context = {'object_list': self.get_queryset()}
		return render(request, self.template_name, context)

#view inheriting from the above class, so we can filter on ID
class MyListView(ClassViewListView):
	queryset = Classview.objects.filter(id=1)		