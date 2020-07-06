from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ArticleForm
from .models import Article



def article_create_view(request):
	form = ArticleForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ArticleForm()  #this clears out the form after saving
	
	context = {
		'form': form
	}
	return render(request, "articles/article_edit.html", context)

def article_update_view(request, id):
	obj = get_object_or_404(Article, id=id)

	form = ArticleForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, "articles/article_edit.html", context)

def article_detail_view(request, id):
	obj = get_object_or_404(Article, id=id)
	context = {
		'object': obj
	}
	return render(request, "articles/article_detail.html", context)


def article_delete_view(request, id):
	obj = get_object_or_404(Article, id=id)
	#confirm POST request
	if request.method == "POST":
		obj.delete()
		return redirect("articles/")
	context = {
		'object': obj
	}
	return render(request, "articles/article_delete.html", context)	


def article_list_view(request):
	queryset = Article.objects.all() #list of objects
	context = {
		"object_list": queryset
	}
	return render(request, "articles/article_list.html", context)	
