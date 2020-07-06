from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm
from .models import Product

def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()  #this clears out the form after saving
	
	context = {
		'form': form
	}
	return render(request, "products/product_edit.html", context)

def product_update_view(request, id):
	obj = get_object_or_404(Product, id=id)
	# above get_object_or_404 is equivalent to this
	# try:
	# 	obj = Product.objects.get(id=id)
	# except Product.DoesNotExist:
	# 	raise Http404

	form = ProductForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, "products/product_edit.html", context)

def product_detail_view(request, id):
	obj = get_object_or_404(Product, id=id)
	context = {
		'object': obj
	}
	return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
	obj = get_object_or_404(Product, id=id)
	#confirm POST request
	if request.method == "POST":
		obj.delete()
		return redirect("products/")
	context = {
		'object': obj
	}
	return render(request, "products/product_delete.html", context)	


def product_list_view(request):
	queryset = Product.objects.all() #list of objects
	context = {
		"object_list": queryset
	}
	return render(request, "products/product_list.html", context)	
