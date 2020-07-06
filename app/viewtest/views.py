from django.shortcuts import render
from django.views import View

# Create your views here.
#Class based view
#base VIEW class = VIEW
class ViewTestView(View):
	template_name = "about.html"
	def get(self, request, *args, **kwargs):
		#return HttpResponse("<h1>About Page</h1>")
		my_context = {
			"my_text": "This is about us",
			"my_number": 123,
			"my_list": [222,333,444,555],
			"my_html": "<h3>Hello World From Class Based View</h3>",
			"title": "This is a test Class Based View"
			}
		return render(request, self.template_name, my_context)


#Function based view to class based view example using about.html
def view_home(request, *args, **kwargs):
	return render(request, 'viewtest/home.html', {})

def my_fbv(request, *args, **kwargs):
	return render(request, 'about.html', {})

def about_view(request, *args, **kwargs):
	#return HttpResponse("<h1>About Page</h1>")
	my_context = {
		"my_text": "This is about us",
		"my_number": 123,
		"my_list": [222,333,444,555],
		"my_html": "<h3>Hello World</h3>",
		"title": "this is a test title"
		}
	return render(request, "about.html", my_context)
