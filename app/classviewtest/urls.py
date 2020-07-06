from django.urls import path
from .views import (
	ClassViewDetailView,
	ClassViewListView,
	MyListView,
	ClassViewCreateView,
	ClassViewUpdateView,
	ClassViewDeleteView
	)
#IMPORTANT: This is a class based view approach, vs a function bases view approach.  
#The class based view requires a specific location/naming convention for the template
# i.e. When looking at a list: appname/modelname_viewname.html  articlesnew/article_list.html
#VERY IMPORTANT!
app_name = 'classview'
urlpatterns = [
 	path('', ClassViewListView.as_view(), name='classview-list'),
 	path('filtered', MyListView.as_view(), name='classviewfiltered-list'),
 	path('blank', ClassViewDetailView.as_view(template_name='contact.html'), name='classview-newrecord'),
    path('<int:id>/', ClassViewDetailView.as_view(), name='classview-detail'),
    path('create/', ClassViewCreateView.as_view(), name='classview-create'),
    path('<int:id>/update/', ClassViewUpdateView.as_view(), name='classview-update'),
    path('<int:id>/delete/', ClassViewDeleteView.as_view(), name='course-delete'),
] 