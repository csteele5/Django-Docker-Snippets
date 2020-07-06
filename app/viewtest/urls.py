from django.urls import path
from .views import (
	view_home,
	my_fbv,
	about_view,
	ViewTestView
	)
#IMPORTANT: This is a class based view approach, vs a function bases view approach.  
#The class based view requires a specific location/naming convention for the template
# i.e. When looking at a list: appname/modelname_viewname.html  articlesnew/article_list.html
#VERY IMPORTANT!
app_name = 'viewtest'
urlpatterns = [
    path('', view_home, name='viewtest-home'),
    path('aboutnc/', my_fbv, name='viewtest-about'),
    path('aboutwc/', about_view, name='viewtest-aboutwc'),
    path('aboutclass/', ViewTestView.as_view(), name='viewtest-aboutclass'),
    path('contact/', ViewTestView.as_view(template_name='contact.html'), name='viewtest-contact'),
] 